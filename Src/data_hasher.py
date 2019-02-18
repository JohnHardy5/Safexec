"""
The main python program that hashes a set of data.

Data can be processed in chunks or as once large piece. The resulting hash is
returned to the code that called it.
"""

import hashlib

CHUNK_SIZE = 64


def grab_chunk(data):
    """Yield a small chunk of data from a large file."""
    start = 0
    while start < len(data):
        chunk = data[start:start + CHUNK_SIZE]
        yield chunk
        start += CHUNK_SIZE
    return


def hash_in_chunks(data):
    """Hash a set of data in chunks."""
    h = hashlib.sha3_512()
    for chunk in grab_chunk(data.encode('utf-8')):
        h.update(chunk)
    return h.hexdigest()
