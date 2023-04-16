#if the files not in the script directory,set a directory.
#look at the format and make it the same for all files
from PyPDF2 import PdfFileMerger
import tkinter as tk
from tkinter import *



merger = PdfFileMerger()

for pdf in range(0,9):
    merger.append("Q{}5.pdf".format(pdf))

merger.write("Preliminary5_208453456_301658852.pdf")
merger.close()






