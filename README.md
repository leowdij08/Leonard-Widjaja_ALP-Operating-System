# SPONGEBOB README

## Introduction
**SPONGEBOB** is a simple Command Line Interface (CLI) tool that provides various functionalities for managing files and directories, performing calculations, and more. The application includes helpful commands like `ls`, `pwd`, `mkdir`, `rmdir`, and some fun extras to enhance the command-line experience.

---

## Features and How to Use

### File and Directory Management
1. **`ls`**
   - **Description**: Lists all files and directories in the current directory.
   - **Usage**:  
     ```
     SPONGEBOB> ls
     ```
   - **Output**: Displays directories in blue and files in cyan.

2. **`pwd`**
   - **Description**: Displays the current working directory.
   - **Usage**:  
     ```
     SPONGEBOB> pwd
     ```

3. **`cd <path>`**
   - **Description**: Changes the current directory to the specified path.
   - **Usage**:  
     ```
     SPONGEBOB> cd path/to/directory
     ```
   - **Example**:  
     ```
     SPONGEBOB> cd ..
     ```

4. **`mkdir <directory name>`**
   - **Description**: Creates a new directory with the specified name.
   - **Usage**:  
     ```
     SPONGEBOB> mkdir new_folder
     ```

5. **`rmdir <directory name>`**
   - **Description**: Removes an empty directory.
   - **Usage**:  
     ```
     SPONGEBOB> rmdir folder_to_remove
     ```

6. **`touch <file name>`**
   - **Description**: Creates an empty file with the specified name.
   - **Usage**:  
     ```
     SPONGEBOB> touch file.txt
     ```

7. **`rm <file name>`**
   - **Description**: Deletes a file. Critical files like `CLIGuy.py` are protected and cannot be removed.
   - **Usage**:  
     ```
     SPONGEBOB> rm file_to_delete.txt
     ```

8. **`cp <src> <target destination>`**
   - **Description**: Copies a file or directory to the target destination.
   - **Usage**:  
     ```
     SPONGEBOB> cp source.txt destination_folder/
     ```

9. **`mv <src> <target destination>`**
   - **Description**: Moves or renames a file or directory.
   - **Usage**:  
     ```
     SPONGEBOB> mv file.txt new_folder/
     ```

### Additional Utilities
1. **`tree`**
   - **Description**: Displays the directory structure in a tree-like format.
   - **Usage**:  
     ```
     SPONGEBOB> tree
     ```

2. **`size <path>`**
   - **Description**: Displays the size of a file or directory in KB.
   - **Usage**:  
     ```
     SPONGEBOB> size path/to/file_or_folder
     ```

3. **`calc <expression>`**
   - **Description**: Evaluates a mathematical expression and prints the result.
   - **Usage**:  
     ```
     SPONGEBOB> calc 20 + 80 * (4 - 1)
     ```

4. **`clear`**
   - **Description**: Clears the terminal screen.
   - **Usage**:  
     ```
     SPONGEBOB> clear
     ```

5. **`help`**
   - **Description**: Displays a list of available commands and their descriptions.
   - **Usage**:  
     ```
     SPONGEBOB> help
     ```

6. **`extra`**
   - **Description**: Lists additional commands and their functions.
   - **Usage**:  
     ```
     SPONGEBOB> extra
     ```

---

### Fun Extras
1. **`joke`**
   - **Description**: Displays a random programming joke.
   - **Usage**:  
     ```
     SPONGEBOB> joke
     ```

2. **`spongebob`**
   - **Description**: A fun Easter egg inspired by the famous anime character.
   - **Usage**:  
     ```
     SPONGEBOB> spongebob
     ```

---

### System Commands
1. **`exit`**
   - **Description**: Exits the CLI with a friendly farewell message.
   - **Usage**:  
     ```
     SPONGEBOB> exit
     ```

---

## Safeguards
- **Critical Files Protection**: Certain critical files (e.g., `CLIGuy.py`, `asset.py`) cannot be removed.
- **Root Directory Protection**: Attempts to navigate to the root directory (`/`) are blocked with a humorous message.

---

## Requirements
- Python 3.6 or higher
- `os` and `shutil` modules (standard libraries)

---
