"""The main unit test suite used to ensure that all source code is bug-free."""

import unittest
import data_hasher


class TestModules(unittest.TestCase):
    """Test all modules in project."""

    def test_data_hasher(self):
        """Test data hasher."""
        test_string = "This is a test string for basic hashing."

        self.assertEqual(
            data_hasher.hash(test_string),
            "c7901b91c1c0be6b1ad74faabb5f57701914e709952be9071a1323732fc6d7ea8feceaddf934e1ca35f1f0c33714b7cb3292bb7b9e6f2cd92821f93491a925bb"
        )


if __name__ == "__main__":
    unittest.main()
