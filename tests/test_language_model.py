import unittest
from src.language_model.language_model import LanguageModel


class TestLanguageModel(unittest.TestCase):
    def setUp(self):
        self.model = LanguageModel()

    def test_generate_text(self):
        prompt = "The future of AI is"
        generated_text = self.model.generate_text(prompt)
        self.assertIsInstance(generated_text, str)
        self.assertTrue(len(generated_text) > len(prompt))
        self.assertTrue(generated_text.startswith(prompt))

    def test_max_length(self):
        prompt = "Once upon a time"
        max_length = 20
        generated_text = self.model.generate_text(prompt, max_length=max_length)
        self.assertLessEqual(len(generated_text), max_length)


if __name__ == "__main__":
    unittest.main()
