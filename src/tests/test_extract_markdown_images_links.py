from unittest import TestCase
from helper_functions.extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownImagesLinks(TestCase):

    def test_it_returns_correct_markdown_image_url_alt(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_it_returns_correct_markdown_links(self):
        matches = extract_markdown_links(
           "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )

        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

        matches = extract_markdown_links(
           "This is text with a link ![to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )

        self.assertListEqual([("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
