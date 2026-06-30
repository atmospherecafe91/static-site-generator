from unittest import TestCase
from helper_functions.block_types import BlockTypes, block_to_block_type_fn


class TestBlockType(TestCase):
    def test_it_return_correct_block_type(self):
        markdown_txt = '1. Hello\n2. World\n3. 4chan'
        block = block_to_block_type_fn(markdown_txt)
        self.assertIs(block, BlockTypes.ORDERED_LIST)

        markdown_txt = '#### Heading'
        block = block_to_block_type_fn(markdown_txt)
        self.assertIs(block, BlockTypes.HEADING)

        markdown_txt = 'This is a random text'
        block = block_to_block_type_fn(markdown_txt)
        self.assertIs(block, BlockTypes.PARAGRAPH)


        markdown_txt = '> THIS IS A QUOTE'
        block = block_to_block_type_fn(markdown_txt)
        self.assertIs(block, BlockTypes.QUOTE)

        markdown_txt = '```\nTHIS IS A QUOTE\n```'
        block = block_to_block_type_fn(markdown_txt)
        self.assertIs(block, BlockTypes.CODE)