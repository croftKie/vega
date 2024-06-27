import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_split_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""

        self.assertEqual(
            ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here', 'This is the same paragraph on a new line', '* This is a list', '* with items'],
            markdown_to_blocks(md)
        )
    
    def test_empty_blocks(self):
        md = """This is **bolded** paragraph


This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line


* This is a list
* with items"""

        self.assertEqual(
            ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here', 'This is the same paragraph on a new line', '* This is a list', '* with items'],
            markdown_to_blocks(md)
        )

    def test_trailing_white_space(self):
        md = """

This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

"""

        self.assertEqual(
            ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here', 'This is the same paragraph on a new line', '* This is a list', '* with items'],
            markdown_to_blocks(md)
        )

    def test_strip_tab_space(self):
        md = """

        This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

"""

        self.assertEqual(
            ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here', 'This is the same paragraph on a new line', '* This is a list', '* with items'],
            markdown_to_blocks(md)
        )

if __name__ == "__main__":
    unittest.main()