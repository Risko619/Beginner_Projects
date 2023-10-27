import os

# Get and print the current working directory
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# Define the file path (replace with your actual file path)
file_path = "/path/to/your/directory/filename.txt"

# Check if the file path exists
if os.path.exists(file_path):
    print("File Path Exists:", file_path)
else:
    print("File Path Does Not Exist:", file_path)
