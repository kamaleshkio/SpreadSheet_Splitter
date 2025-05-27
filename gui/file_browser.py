from tkinter import filedialog, Tk

def choose_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    return file_path

def choose_output_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    return folder_path