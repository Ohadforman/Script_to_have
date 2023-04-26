classdef CodeChecker < handle
    % CODECHECKER - Class for evaluating code from ChatGPT
    %   CodeChecker is a class that can extract code from ChatGPT
    %   responses, run the code with a unit testing framework, and return
    %   the test results in a format for display in a chat window. Each
    %   input message from ChatGPT gets its own test folder to hold the
    %   generated code and artifacts like test results and images
    %
    %   Example:
    %
    %       % Get a message from ChatGPT
    %       myBot = chatGPT();
    %       response = send(myBot,"Create a bar plot in MATLAB.");
    %
    %       % Create object
    %       checker = CodeChecker(response);
    %
    %       % Check code for validity and display test report
    %       runChecks(checker);
    %       report = checker.Report;

    properties (SetAccess=private)
        ChatResponse % ChatGPT response that may have code 
        OutputFolder % Full path with test results
        Results % Table with code check results
        Timestamp % Unique string with current time to use for names
        Artifacts % List of files generated by the checks
        ErrorMessages % Cell str of any error messages from results
        Report % String with the nicely formatted results
    end

    methods
        %% Constructor
        function obj = CodeChecker(inputStr,pathStr)
            %CODECHECKER Constructs an instance of this class
            %    checker = CodeChecker(message) creates an instance
            %    of the CodeChecker class given a response from
            %    ChatGPT in the string "message".
            arguments
                inputStr string {mustBeTextScalar}
                pathStr string {mustBeTextScalar} = "";
            end
            obj.ChatResponse = inputStr;
            if pathStr == ""
                s = dir;
                pathStr = s(1).folder;
            end
            % Construct a unique output folder name using a timstamp
            obj.Timestamp = string(datetime('now','Format','yyyy-MM-dd''T''HH-mm-SS'));
            obj.OutputFolder = fullfile(pathStr,"contents","GeneratedCode","Test-" + obj.Timestamp);

            % Empty Results table
            obj.Results = [];
        end
    end
    methods (Access=public)
        function runChecks(obj)
            % RUNCHECKS - Run generated code and check for errors
            %   runChecks(obj) will run each piece of generated code. NOTE:
            %   This function does not check generated code for
            %   correctness, just validity
    
            % make the output folder 
            mkdir(obj.OutputFolder)

            % Get list of current files so we know which artifacts to move
            % to the output folder
            filesBefore = dir();                    
    
            % save code files and get their names for testing;
            saveCodeFiles(obj);
    
            % Run all test files
            runCodeFiles(obj);

            % Move all newly generated files
            filesAfter = dir();                        
            obj.Artifacts = string(setdiff({filesAfter.name},{filesBefore.name}));
            for i = 1:length(obj.Artifacts)
                movefile(obj.Artifacts(i),obj.OutputFolder)
            end

            % Fill the results properties like Report and ErrorMessages
            processResults(obj)
        end
    end

    methods(Access=private)
        function saveCodeFiles(obj)
            % SAVECODEFILES Saves M-files for testing
            %    saveCodeFiles(obj) will parse the ChatResponse propety for
            %    code blocks and save them to separate M-files with unique
            %    names in the OutputFolder property location

            % Extract code blocks
            [startTag,endTag] = TextHelper.codeBlockPattern();
            codeBlocks = extractBetween(obj.ChatResponse,startTag,endTag);

            % Create Results table
            obj.Results = table('Size',[length(codeBlocks) 4],'VariableTypes',["string","string","string","logical"], ...
                'VariableNames',["ScriptName","ScriptContents","ScriptOutput","IsError"]);
            obj.Results.ScriptContents = codeBlocks;

            % Save code blocks to M-files
            for i = 1:height(obj.Results)
                % Open file with the function name or a generic test name.
                obj.Results.ScriptName(i) = "Test" + i + "_" + replace(obj.Timestamp,"-","_");
                fid = fopen(obj.Results.ScriptName(i) + ".m","w");                

                % Add the code to the file
                fprintf(fid,"%s",obj.Results.ScriptContents(i));
                fclose(fid);
            end
        end

        function runCodeFiles(obj)
            % RUNCODEFILES - Tries to run all the generated scripts and
            % captures outputs/figures

            % Before tests, make existing figure handles invisible
            figsBefore = findobj('Type','figure');
            for i = 1:length(figsBefore)
                figsBefore(i).HandleVisibility = "off";
            end

            % Also check for open and closed Simulink files            
            addOns = matlab.addons.installedAddons;
            addOns = addOns(addOns.Name=="Simulink",:);
            hasSimulink = ~isdeployed && ~isempty(addOns) && addOns.Enabled;
            if hasSimulink
                BDsBefore = find_system('SearchDepth',0);
                SLXsBefore = dir("*.slx");
                SLXsBefore = {SLXsBefore.name}';
            end

            % Iterate through scripts. Run the code and capture any output
            for i = 1:height(obj.Results)
                try 
                    output = evalc(obj.Results.ScriptName(i));
                    if isempty(output)
                        output = "This code did not produce any output";
                    end
                    obj.Results.ScriptOutput(i) = output;    
                catch ME
                    obj.Results.IsError(i) = true;
                    obj.Results.ScriptOutput(i) = TextHelper.shortErrorReport(ME);
                end
            end

            % Find newly Simulink models            
            if hasSimulink
                BDsNew = setdiff(find_system("SearchDepth",0),BDsBefore);
                BDsNew(BDsNew=="simulink") = [];
                SLXsfiles = dir("*.slx");
                SLXsNew = setdiff({SLXsfiles.name}',SLXsBefore);
                SLXsNew = extractBefore(SLXsNew,".slx");
    
                % Load the new SLX-files. Add to list of new BDs
                for i = 1:length(SLXsNew)
                    load_system(SLXsNew{i});
                end
                BDsNew = union(BDsNew,SLXsNew);
    
                % Print screenshots for the new BDs. Then save and close them
                for i = 1:length(BDsNew)
                    print("-s" + BDsNew{i},"-dpng",BDsNew{i} + ".png");
                    save_system(BDsNew{i});
                    close_system(BDsNew{i});
                end
            end

            % Save new figures as png and reset the old figures as visible
            figsAfter = findobj("Type","figure");
            for i = 1:length(figsAfter)
                saveas(figsAfter(i),"Figure" + i + ".png");                                
            end
            for i = 1:length(figsBefore)
                figsBefore(i).HandleVisibility = "on";
            end
        end

        function processResults(obj)
            % PROCESSRESULTS - Process the test results
            %
            %   processResults(obj) will assign values to the properties
            %   Report and ErrorMessages. obj.Report is a string with a
            %   nicely formatted report, and obj.ErrorMessages is a cellstr
            %   with any error messages
            %

            % Get the error messages from the Results table
            obj.ErrorMessages = obj.Results.ScriptOutput(obj.Results.IsError);

            % Set up the report header
            numBlocks = height(obj.Results);
            numErrors = length(obj.ErrorMessages);
            reportHeader = sprintf(['<div class="test-report"><p>Here are the test results. ' ...
                'There were <b>%d code blocks</b> tested and <b>%d errors</b>.</p>'], ...
                numBlocks,numErrors);

            % Handle plurals
            if numBlocks == 1 
                reportHeader = replace(reportHeader,'were','was');
                reportHeader = replace(reportHeader,'blocks','block');
            end
            if numErrors == 1
                reportHeader = replace(reportHeader,'errors','error');
            end

            % Loop through results table to make the report
            testReport = reportHeader;
            for i = 1:height(obj.Results)

                % Start the report with the script name
                testReport = [testReport sprintf('<div class="test"><p><b>Test:</b> %s</p>', ...
                    obj.Results.ScriptName(i))]; %#ok<AGROW>

                % Use error style if code produced an error
                codeBlockClass = "test-block-green";
                if obj.Results.IsError(i)
                    codeBlockClass = "test-block-red";
                end
                
                % Add code
                testReport = [testReport sprintf('<code class=%s>%%%% Code: \n\n%s\n\n', ...
                    codeBlockClass,obj.Results.ScriptContents(i))]; %#ok<AGROW>

                % Add output
                testReport = [testReport sprintf('%%%% Command Window Output: \n\n%s', ...
                    obj.Results.ScriptOutput(i))]; %#ok<AGROW>

                % Add the closing tags
                testReport = [testReport '</code></div>']; %#ok<AGROW>
            end

            % Show any image artifacts
            imageFiles = obj.Artifacts(contains(obj.Artifacts,".png"));
            folders = split(obj.OutputFolder,filesep);
            if ~isempty(imageFiles)
                testReport = [testReport '<div class="figures"><p><b>Figures</b></p>']; 
                for i = 1:length(imageFiles)
                    % Get the relative path of the image. Assumes that the HTML
                    % file is at the same level as the "GeneratedCode" folder                
                    relativePath = fullfile(folders(end-1),folders(end),imageFiles(i));
                    relativePath = replace(relativePath,'\','/');
    
                    % Assemble the html code for displaying the image
                    testReport = [testReport sprintf('<div class="figure"><img src="%s" class="ml-figure"/></div>',relativePath)]; %#ok<AGROW>
                end
                testReport = [testReport '</div>']; 
            end

            % List the artifacts
            testReport = [testReport '<div class="artifacts"><p><b>Artifacts</b></p>']; 
            testReport = [testReport sprintf('<code class="code-block">The following artifacts were saved to: %s\n\n',obj.OutputFolder)];
            for i = 1:length(obj.Artifacts)
                testReport = [testReport sprintf('     %s\n',obj.Artifacts(i))]; %#ok<AGROW>
            end
            testReport = [testReport '</code></div>']; 
            
            % Close the initial div for the overall report
            testReport = [testReport '</div>']; 
            
            % Assign testReport to Report property
            obj.Report = testReport;
        end
    end
end