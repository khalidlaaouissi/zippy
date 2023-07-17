import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def extract_file(file_path, destination_path, password=None):
    file_name = os.path.basename(file_path)
    file_name_without_ext, file_ext = os.path.splitext(file_name)
    extract_path = os.path.join(destination_path, file_name_without_ext)

    try:
        if file_ext == '.zip':
            if password:
                command = f'7z x -p"{password}" -y -o"{extract_path}" "{file_path}"'
            else:
                command = f'7z x -y -o"{extract_path}" "{file_path}"'

            os.system(command)
        elif file_ext == '.rar':
            if password:
                command = f'7z x -p"{password}" -y -o"{extract_path}" "{file_path}"'
            else:
                command = f'7z x -y -o"{extract_path}" "{file_path}"'

            os.system(command)
        else:
            print(f"Unsupported file format: {file_path}")
            return

        print(f"Extracted: {file_path}")
        return extract_path
    except Exception as e:
        print(f"Failed to extract {file_path}: {str(e)}")
        return None

def delete_file_with_retry(file_path):
    max_attempts = 3
    attempt = 1
    while attempt <= max_attempts:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
            return
        except PermissionError:
            print(f"Failed to delete {file_path}. The file might still be in use. Retrying...")
            time.sleep(1)
            attempt += 1

    print(f"Exceeded maximum deletion attempts. Failed to delete: {file_path}")

def unzip_files_in_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            password = simpledialog.askstring("Password", f"Enter password for {file_path} (leave blank if none)")
            extract_path = extract_file(file_path, directory, password)
            if extract_path:
                delete_zip = messagebox.askquestion("Delete Confirmation", f"Do you want to delete {file_path} after extraction?")
                if delete_zip == 'yes':
                    time.sleep(1)  # Add a delay of 1 second
                    delete_file_with_retry(file_path)
                else:
                    print(f"Skipped deletion: {file_path}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        unzip_files_in_directory(directory)

# Create the main window
window = tk.Tk()
window.title("File Extractor")

# Create a button to select the directory
select_button = tk.Button(window, text="Select Directory", command=select_directory)
select_button.pack(padx=10, pady=10)

# Run the GUI event loop
window.mainloop()