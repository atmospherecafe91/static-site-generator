from unittest import TestCase
from helper_functions.generate_page import extract_title


class TestExtractMarkdownHeader(TestCase):
    def test_it_returns_correct_title(self):
        text = """

###### I love you 3000

I also love iron man


"""
        self.assertEqual("I love you 3000", extract_title(text))

    def test_it_raises_error_on_no_headers(self):
        text = """

    Captain American is such a bad-ass hero!!!


"""     
        with self.assertRaises(Exception):
            extract_title(text)