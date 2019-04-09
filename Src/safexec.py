"""
Pulls a file location from the command line and signs or checks said file.

The sign() function takes a .ELF file and hashes the contents, placing the
hash at the end of the file. The file is then renamed as a .ELFS file (this
stands for ELF Secure).

The check() function takes a .ELFS file and removes the hash from the end
of the file. The remaining contents are hashed and the two hashes are compared.
If the two are the same, the function returns a positive indication that the
file is safe to run. Otherwise, a negative indication is returned instead.
"""

import sys
import file_handler
import data_hasher


def sign(f):
    """Sign ELF file. Change file to ELFS."""
    hash = data_hasher.hash_file(f)
    file_handler.create_elfs(f, hash)


def check(f):
    """Check ELFS file."""
    given_hash = file_handler.pull_hash_from_file(f)
    elf = file_handler.create_elf(f)
    actual_hash = data_hasher.hash_file(elf)
    elf.close()
    if given_hash == actual_hash:
        print("File provided is safe-to-execute.")
    else:
        print("File provided is NOT safe-to-execute.")


file, extension = file_handler.open_file(sys.argv[1])
if extension is ".ELF":
    sign(file)
else:
    check(file)

file.close()
