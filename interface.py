import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import convert

def select_read_path(label):

    global read_path
    directory = filedialog.askdirectory(title="Select the folder with audio files you want to convert:")

    if directory:
        label.config(text=f"Read Path: {directory}")
        read_path = directory

def select_write_path(label):

    global write_path
    directory = filedialog.askdirectory(title="Select the folder where you want to export converted audio:")

    if directory:
        label.config(text=f"Write Path: {directory}")
        write_path = directory

def run(file_format):
    window = tk.Toplevel()
    window.geometry("400x90")
    window.wm_title("Converting Files...")
    window.update_idletasks() # show the window
    convert.mass_convert(read_path + "/", write_path + "/", file_format.get())
    messagebox.showinfo("Converted", "Files successfully converted")
    window.destroy()
    root.destroy()


read_path = ""
write_path = ""
root = tk.Tk()
root.geometry("400x500")
root.title("Mass Audio Converter")

selected_file_label_1 = tk.Label(root, text="Read Path:")
selected_file_label_1.pack()

select_button_read = tk.Button(root, text="Select read directory", command=lambda: select_read_path(selected_file_label_1))
select_button_read.pack(padx=20, pady=20)

selected_file_label_2 = tk.Label(root, text="Write Path:")
selected_file_label_2.pack()

selectButton2 = tk.Button(root, text="Select write directory", command=lambda: select_write_path(selected_file_label_2))
selectButton2.pack(padx=20, pady=20)

format_label = tk.Label(root, text="Format to convert to:")
format_label.pack(padx=20, pady=20)

options = {"aac", "flv", "mp3", "m4a", "ogg", "wav", "wma"}
selected_format = tk.StringVar(root)
selected_format.set("mp3")
format_menu = tk.OptionMenu(root, selected_format, *options)
format_menu.pack(padx=20, pady=20)


runButton = tk.Button(root, text="Convert", command=lambda: run(selected_format))
runButton.pack(padx=20, pady=10)

root.mainloop()