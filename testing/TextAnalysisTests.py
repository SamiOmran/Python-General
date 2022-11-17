import unittest
import os

from textanalyzer import analyze_text


class TextAnalysisTests(unittest.TestCase):
    """Unit test for the ``analysis_text()`` function"""

    def setUp(self):
        """Fixture that runs before avery test method
            to save the text file path
        """
        self.file = 'text_analysis_test_file.txt'
        with open(self.file, 'wt') as f:
            f.write('I am writing to the file\n'
                    'and now?\n'
                    '\n'
                    '.')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.file)
        except OSError:
            pass

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        analyze_text(self.file)

    def test_line_count(self):
        """Chek if the line count is correct"""
        self.assertEqual(analyze_text(self.file)[0], 4)

    def test_character_count(self):
        """Check the number of characters in the file"""
        self.assertEqual(analyze_text(self.file)[1], 36)

    def test_no_such_file(self):
        """Check if the test fail when the file not exists"""
        with self.assertRaises(IOError):
            analyze_text('foo')

    def test_no_deletion(self):
        """Check the function does not delete the file"""
        analyze_text(self.file)
        self.assertTrue(os.path.exists(self.file))


if __name__ == '__main__':
    unittest.main()
