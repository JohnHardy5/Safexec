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
import safexec_exceptions
import file_handler
import data_hasher


def sign(file):
    """Sign ELF file. Change file to ELFS."""
    file_hash = data_hasher.hash_file(file)
    file_handler.create_elfs(file, file_hash)


def check(file):
    """Check ELFS file."""
    given_hash = file_handler.pull_hash_from_file(file)
    elf = file_handler.create_elf(file)
    actual_hash = data_hasher.hash_file(elf)
    elf.close()
    if given_hash == actual_hash:
        print("File provided is safe-to-execute.")
    else:
        print("File provided is NOT safe-to-execute.")


if len(sys.argv) < 2:
    raise safexec_exceptions.NotEnoughArgsError

FILE, EXTENSION = file_handler.open_file(sys.argv[1])
if EXTENSION == ".ELF":
    sign(FILE)
else:
    check(FILE)

FILE.close()
