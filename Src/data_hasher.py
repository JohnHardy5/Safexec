"""
The main python program that hashes a set of data.

Data can be processed in chunks or as once large piece. The resulting hash is
returned to the code that called it.
"""

import hashlib

CHUNK_SIZE = 1024


def hash_data(data):
    """Hash a string in one big piece."""
    hash_alg = hashlib.sha3_512()
    hash_alg.update(data)
    return hash_alg.hexdigest()


def grab_chunk(data):
    """Yield a small chunk of data from a large file."""
    start = 0
    while start < len(data):
        chunk = data[start:start + CHUNK_SIZE]
        yield chunk
        start += CHUNK_SIZE


def hash_in_chunks(data):
    """Hash a set of data in chunks."""
    hash_alg = hashlib.sha3_512()
    for chunk in grab_chunk(data.encode('utf-8')):
        hash_alg.update(chunk)
    return hash_alg.hexdigest()
