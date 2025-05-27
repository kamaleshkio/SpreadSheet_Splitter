from tkinter import filedialog, Tk

def Choose_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    return file_path

def Choose_output_folder():
    root = Tk()
    root.withdraw()  # Hide the root window
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    return output_folder