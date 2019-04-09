"""
The main python program that hashes a set of data.

Data can be processed in chunks or as once large piece. The resulting hash is
returned to the code that called it.
"""

import hashlib

FILE_CHUNK_SIZE = 1024


def hash_string(string):
    """Hash a string in one big piece."""
    h = hashlib.sha3_512()
    h.update(string.encode("utf-8"))
    return h.hexdigest()


def grab_chunk(file):
    """Yield a small chunk of data from a large file."""
    start = 0
    while start < len(file):
        chunk = file[start:start + FILE_CHUNK_SIZE]
        yield chunk
        start += FILE_CHUNK_SIZE


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
