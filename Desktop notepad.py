import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

root = tk.Tk()
root.title("Notepad")

text_area = tk.Text(root)
text_area.pack(expand=True, fill="both")

tk.Button(root, text="Open", command=open_file).pack(side="left")
tk.Button(root, text="Save", command=save_file).pack(side="right")

root.mainloop()
