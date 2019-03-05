"""The main unit test suite used to ensure that all source code is bug-free."""

import unittest
import data_hasher
import file_handler

def to_binary(string):
    """Convert string to binary"""
    print(''.join(format(x, 'b') for x in bytearray(string, "utf-8")))
    return ''.join(format(x, 'b') for x in bytearray(string, "utf-8"))

class TestModules(unittest.TestCase):
    """Test all modules in project."""

    def test_hasher(self):
        """Test non-chunk based data hasher."""
        empty_string = ""
        test_string = "this is a test string"
        test_bytes = to_binary("this is a test string")

        self.assertEqual(
            data_hasher.hash_string(empty_string),
            "a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26" # pylint: disable=line-too-long
        )

        self.assertEqual(
            data_hasher.hash_string(test_string),
            "a88e43eb3b3627f9864679ece6b613497caa2f55f5efa309fe02e964b7ead7722e1bba710ed746d89962f84636c21a9a2a02a6c89d1fd99f9ac6a6fef7e6a32a" # pylint: disable=line-too-long
        )

        self.assertEqual(
            data_hasher.hash_string(test_bytes),
            "47c34fa5a116e04a9fe89e610ec5ee319cbccd6fc440e7f0b0bccd14d6593a7af9e910b07d5af44861283c29e67e79322a55d83333de0991d349e6f80acd5b64" # pylint: disable=line-too-long
        )

    def test_chunk_hasher(self):
        """Test chunk based data hashing."""
        empty = ""
        lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." # pylint: disable=line-too-long
        chunk_size = 8

        self.assertEqual(
            data_hasher.hash_in_chunks(empty, chunk_size),
            "a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26" # pylint: disable=line-too-long
        )

        self.assertEqual(
            data_hasher.hash_in_chunks(lorem, chunk_size),
            "f32a9423551351df0a07c0b8c20eb972367c398d61066038e16986448ebfbc3d15ede0ed3693e3905e9a8c601d9d002a06853b9797ef9ab10cbde1009c7d0f09" # pylint: disable=line-too-long
        )

    def test_file_hasher(self):
        """Test file hashing on simple files as well as large ones."""
        text_file_path = "test_file.txt"
        empty_file_path = "empty_file.txt"
        doc_file_path = "test_file.docx"
        mp4_file_path = "test_file.mp4"

        file = open(text_file_path, "rb")
        self.assertEqual(
            data_hasher.hash_file(file),
            "ef90bed878786313589b4c1458cf19b5cd8d0059239b3dd726ca8ba1bc803f361830c78c764f91163624f5b4e9d77435adc200e7a692be28b0f76680c3ee3e67" # pylint: disable=line-too-long
        )
        file.close()

        file = open(empty_file_path, "rb")
        self.assertEqual(
            data_hasher.hash_file(file),
            "a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26" # pylint: disable=line-too-long
        )
        file.close()

        file = open(doc_file_path, "rb")
        self.assertEqual(
            data_hasher.hash_file(file),
            "deaa5f3177edd910a4b2086df7e795506b45cd43129a7159ef1dda69a37b42eff1a07c9be77b8f9e148bc4db053fa2265e9fbd303bbd85116714f2f411bf5e2f" # pylint: disable=line-too-long
        )
        file.close()

        file = open(mp4_file_path, "rb")
        self.assertEqual(
            data_hasher.hash_file(file),
            "9627db1a4587e1ceb473f0afce7ea62c7e20ff43463aef64dbe73992184199ec0c43836283cc16321c831ea7a00d9e70a82ccdc083a13ee7aabf84e8523e1c75" # pylint: disable=line-too-long
        )
        file.close()

    def test_file_opener:


if __name__ == "__main__":
    unittest.main()
