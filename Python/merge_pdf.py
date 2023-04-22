import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from PyPDF2 import PdfFileMerger

Builder.load_string("""
<MergePDFs>:
    orientation: 'vertical'
    padding: 10

    # Input file path
    TextInput:
        id: input_path
        hint_text: 'Input file path'
        multiline: False

    # Output directory path
    TextInput:
        id: output_directory
        hint_text: 'Output directory path'
        multiline: False

    # Prefix of input file names
    TextInput:
        id: input_prefix
        hint_text: 'Input file prefix'
        multiline: False

    # Output file name
    TextInput:
        id: output_file_name
        hint_text: 'Output file name'
        multiline: False

    Button:
        text: 'Merge PDFs'
        on_press: root.merge_pdfs()
""")

class MergePDFs(BoxLayout):
    def merge_pdfs(self):
        # Get user inputs
        input_path = self.ids.input_path.text
        output_directory = self.ids.output_directory.text
        input_prefix = self.ids.input_prefix.text
        output_file_name = self.ids.output_file_name.text

        # Create a list of PDF files in alphanumeric order
        pdf_files = sorted(
            [
                os.path.join(input_path, filename)
                for filename in os.listdir(input_path)
                if filename.startswith(input_prefix) and filename.endswith(".pdf")
            ]
        )

        # Create a PDF file merger object
        pdf_merger = PdfFileMerger()

        # Merge the PDF files in alphanumeric order
        for pdf_file in pdf_files:
            pdf_merger.append(pdf_file)

        # Save the merged PDF to a file with .pdf extension
        output_path = os.path.join(output_directory, output_file_name + ".pdf")
        with open(output_path, "wb") as output_file:
            pdf_merger.write(output_file)

        print("PDFs merged successfully!")

class MergePDFsApp(App):
    def build(self):
        return MergePDFs()

if __name__ == "__main__":
    MergePDFsApp().run()
