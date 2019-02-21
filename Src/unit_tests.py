"""The main unit test suite used to ensure that all source code is bug-free."""

import unittest
import data_hasher

def to_binary(string):
    """Convert string to binary"""
    return ''.join(format(x, 'b') for x in bytearray(string, "utf-8"))

class TestModules(unittest.TestCase):
    """Test all modules in project."""

    def test_hasher(self):
        """Test non-chunk based data hasher."""
        test_string = "this is a test string".encode("utf-8")
        test_bytes = to_binary("this is a test string").encode("utf-8")

        self.assertEqual(
            data_hasher.hash_data(test_string),
            "a88e43eb3b3627f9864679ece6b613497caa2f55f5efa309fe02e964b7ead7722e1bba710ed746d89962f84636c21a9a2a02a6c89d1fd99f9ac6a6fef7e6a32a" # pylint: disable=line-too-long
        )
        self.assertEqual(
            data_hasher.hash_data(test_bytes),
            "47c34fa5a116e04a9fe89e610ec5ee319cbccd6fc440e7f0b0bccd14d6593a7af9e910b07d5af44861283c29e67e79322a55d83333de0991d349e6f80acd5b64" # pylint: disable=line-too-long
        )


if __name__ == "__main__":
    unittest.main()
