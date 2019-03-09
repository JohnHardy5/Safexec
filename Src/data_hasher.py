"""
The main python program that hashes a set of data.

Data can be processed in chunks or as once large piece. The resulting hash is
returned to the code that called it.
"""

import hashlib

FILE_CHUNK_SIZE = 1024

def hash_string(string):
    """Hash an entire encoded string of data."""
    hash_alg = hashlib.sha3_512()
    hash_alg.update(string.encode("utf-8"))
    return hash_alg.hexdigest()


def grab_chunk(data, chunk_size):
    """Yield a small chunk of data from a larger piece."""
    start = 0
    while start < len(data):
        chunk = data[start:start + chunk_size]
        yield chunk
        start += chunk_size


def hash_in_chunks(data, chunk_size):
    """Hash a set of data in chunks."""
    hash_alg = hashlib.sha3_512()
    for chunk in grab_chunk(data.encode("utf-8"), chunk_size):
        hash_alg.update(chunk)
    return hash_alg.hexdigest()


def hash_file(file):
    """Hash file provided."""
    hash_alg = hashlib.sha3_512()
    while True:
        data = file.read(FILE_CHUNK_SIZE)
        if not data:
            break
        hash_alg.update(data)
    return hash_alg.hexdigest()

def sign_elf(file_path):
    """Sign an ELF file if it is valid."""

def check_elfs(file_path):
    """Check an ELFS signature if it is valid."""
