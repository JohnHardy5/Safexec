"""
Used to manage files and handle signing or checking the signature of a file.

The sign() function takes a .ELF file and hashes the contents, placing the
hash at the end of the file. The file is then renamed as a .ELFS file (this
stands for ELF Secure).

The check() function takes a .ELFS file and removes the hash from the end
of the file. The remaining contents are hashed and the two hashes are compared.
If the two are the same, the function returns a positive indication that the
file is safe to run. Otherwise, a negative indication is returned instead.
"""

import os.path

def open_file(path):
    """Test a given path to see if it leads to a valid file. If so, open it."""
    file_ext = os.path.splitext(path)[1]
    if ('.ELF', '.ELFS') not in file_ext:
        print("ERROR! Bad file given.")
    return None


def sign(file_path):
    """Sign ELF file. Change file to ELFS."""
    return None

def check():
    """Check ELFS file."""
    return None
