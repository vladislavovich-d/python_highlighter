import unittest
from highlighter import create_app

class HighlightTest(unittest.TestCase):

    def setUp(self):

        self.app = create_app().test_client()

        # TODO: add the missing test data in this routine

        self.highlighted_text = b'Sample <mark>text</mark> to be highlighted'
        self.search_text = b'Text'
        self.text = b'Sample text to be highlighted'

    def tearDown(self):

        # TODO: add an implementation

        del self.app
        del self.highlighted_text
        del self.text
        del self.search_text

    def test_markup_text(self):
        """Test markup process"""
        response = self.app.post('/', data={'search': self.search_text,
                                            'text': self.text})
        self.assertIn(self.highlighted_text, response.data)
