import os

# Function to print the contents of a directory
def print_directory_contents(path):
    try:
        # Get the list of all files and directories
        dir_contents = os.listdir(path)
        
        # Print the contents
        for item in dir_contents:
            print(item)
    
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '.'  # Current directory
print_directory_contents(directory_path)
