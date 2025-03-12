import os
import sys
import time

# Check if the user provided a file path as an argument
if len(sys.argv) != 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

# Get the file path, resolving '~' to the user's home directory
file_path = os.path.expanduser(sys.argv[1])

# Print the current process ID
print("Process ID:", os.getpid())

# Open the file in read/write mode
try:
    fd = os.open(file_path, os.O_RDWR)  # Open file for reading and writing
    with os.fdopen(fd, "r+") as f:  # Use fdopen to wrap the file descriptor in a file object
        print(f.fileno())  # Print the file descriptor number
        time.sleep(9999)  # Sleep for 9999 seconds (for demonstration purposes)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except PermissionError:
    print(f"Permission denied: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
