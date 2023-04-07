import tkinter as tk
from tkinter import filedialog
from functools import partial
from image import add_watermark


# def start_watching():
#     folder_path = folder_path_var.get()
#     watermark_path = watermark_path_var.get()
#     width = int(width_var.get())
#     opacity = float(opacity_var.get())
#     scale = float(scale_var.get())
#     position = position_var.get()
#
#     add_watermark(folder_path, watermark_path, width, opacity, scale, position)


def create_gui():
    def browse_folder_path():
        folder_path = filedialog.askdirectory()
        folder_path_var.set(folder_path)

    def browse_watermark_path():
        watermark_path = filedialog.askopenfilename(filetypes=(("Image files", "*.jpg;*.png"),))
        watermark_path_var.set(watermark_path)

    root = tk.Tk()
    root.title("Watch Folder with Watermark")
    root.geometry("500x300")

    folder_path_label = tk.Label(root, text="Folder Path:")
    folder_path_label.pack()
    folder_path_var = tk.StringVar()
    folder_path_entry = tk.Entry(root, textvariable=folder_path_var)
    folder_path_entry.pack()
    browse_folder_path_button = tk.Button(root, text="Browse", command=browse_folder_path)
    browse_folder_path_button.pack()

    watermark_path_label = tk.Label(root, text="Watermark Path:")
    watermark_path_label.pack()
    watermark_path_var = tk.StringVar()
    watermark_path_entry = tk.Entry(root, textvariable=watermark_path_var)
    watermark_path_entry.pack()
    browse_watermark_path_button = tk.Button(root, text="Browse", command=browse_watermark_path)
    browse_watermark_path_button.pack()

    width_label = tk.Label(root, text="Watermark Width:")
    width_label.pack()
    width_var = tk.StringVar(value="100")
    width_entry = tk.Entry(root, textvariable=width_var)
    width_entry.pack()

    opacity_label = tk.Label(root, text="Watermark Opacity:")
    opacity_label.pack()
    opacity_var = tk.StringVar(value="0.5")
    opacity_entry = tk.Entry(root, textvariable=opacity_var)
    opacity_entry.pack()

    scale_label = tk.Label(root, text="Watermark Scale:")
    scale_label.pack()
    scale_var = tk.StringVar(value="0.1")
    scale_entry = tk.Entry(root, textvariable=scale_var)
    scale_entry.pack()

    position_label = tk.Label(root, text="Watermark Position:")
    position_label.pack()
    position_var = tk.StringVar(value="br")
    position_entry = tk.Entry(root, textvariable=position_var)
    position_entry.pack()

    def start_watching():
        folder_path = folder_path_var.get()
        watermark_path = watermark_path_var.get()
        width = int(width_var.get())
        opacity = float(opacity_var.get())
        scale = float(scale_var.get())
        position = position_var.get()

        add_watermark(folder_path, watermark_path, width, opacity, scale, position)

    start_watching_button = tk.Button(root, text="Start Watching", command=start_watching)
    start_watching_button.pack()

    root.mainloop()


if __name__ == '__main__':
    create_gui()
