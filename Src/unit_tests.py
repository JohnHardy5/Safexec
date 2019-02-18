"""The main unit test suite used to ensure that all source code is bug-free."""

import unittest
import data_hasher
import test_file


def test_data_hasher():
    """Test data hasher."""
    test_string = "This is a test string for basic hashing."
    print(data_hasher.hash(test_string))


def main():
    """Execute tests."""
    test_data_hasher()


if __name__ == "__main__":
    main()
