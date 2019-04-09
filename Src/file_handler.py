"""
Used to manage files and change them.

Files can be opened, copied, or modified in order to prepare them for other
operations such as hashing or signing.
"""

import os
import shutil
import safexec_exceptions


def open_file(path):
    """Test a given path to see if it leads to a valid file. If so, open it."""
    file_ext = os.path.splitext(path)[1]
    if file_ext not in ('.ELF', '.ELFS'):
        raise safexec_exceptions.FileExtensionError
    if not os.path.exists(path):
        raise safexec_exceptions.FilePathError
    if not os.path.isfile(path):
        raise FileNotFoundError
    return [open(path, "rb"), file_ext]


def pull_hash_from_file(file):
    """Return the last 64 bytes of a file if it is a hash."""
    #file_hash = file
    print("Pull hash")


def create_elf(file):
    """Create an ELF file from an ELFS file."""
    print("create elf")


def create_elfs(file, file_hash):
    """Create an ELFS file from an ELF file and a hash."""
    file_path = os.path.abspath(file.name)
    new_file_path = file_path + "S"
    shutil.copyfile(file_path, new_file_path)
    new_file = open(new_file_path, "a")
    new_file.write(file_hash)
    new_file.close()
