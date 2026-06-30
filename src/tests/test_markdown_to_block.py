from unittest import TestCase

from helper_functions.markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlock(TestCase):
    def test_it_returns_the_right_markdown(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_it_removes_empty_blocks(self):
        md = """


            empty blocks


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ['empty blocks']
        )