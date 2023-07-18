# Zippy

Zippy is a simple file extractor tool built with Tkinter in Python. It allows you to select a directory and extract files within that directory using the 7-Zip command-line tool.

## Prerequisites

Before running the code, make sure you have the following requirements:

- Python installed on your system
- 7-Zip command-line tool installed and added to your system's PATH

## Usage

1. Clone the repository or copy the code from the provided snippet.

2. Install the required packages using the following command:

```bash
pip install tkinter
```

3. Run the code using the following command:

```bash
python zippy.py
```

4. The Zippy window will open.

5. Click the "Select Directory" button to choose the directory containing the files you want to extract.

6. If any files require a password for extraction, you will be prompted to enter it.

7. After extraction, you will be asked if you want to delete the original zip files. Choose accordingly.

## Important Note

Ensure that you have the 7-Zip command-line tool installed on your system and added to your PATH. The tool is required for file extraction.

## Additional Information

Zippy utilizes the `tkinter` library for creating the graphical user interface (GUI) and the `os` and `time` modules for file operations and management.

The code provides functions to extract files, delete files, and unzip files in a directory. It also includes a GUI window created with Tkinter, where you can select the directory and initiate the extraction process.

Feel free to customize the code according to your specific needs. You can modify the GUI layout, add additional functionality, or integrate it into your own projects.

Happy file extraction with Zippy!
