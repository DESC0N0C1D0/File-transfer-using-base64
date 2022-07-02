import base64
import pyperclip
from tkinter import *
from tkinter import filedialog
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "./", title = "Select file")
with open(root.filename, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
x = root.filename.split("/")
pyperclip.copy(f"echo '{encoded_string.decode('utf-8')}' | base64 --decode > {x[-1]}\n")
