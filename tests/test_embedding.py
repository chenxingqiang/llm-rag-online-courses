import unittest
import numpy as np
from src.embedding.embedding_model import EmbeddingModel


class TestEmbeddingModel(unittest.TestCase):
    def setUp(self):
        self.model = EmbeddingModel()

    def test_get_embedding(self):
        text = "Hello, world!"
        embedding = self.model.get_embedding(text)
        self.assertIsInstance(embedding, np.ndarray)
        self.assertEqual(embedding.shape, (768,))  # Assuming BERT base model

    def test_different_texts_different_embeddings(self):
        text1 = "Hello, world!"
        text2 = "Goodbye, world!"
        embedding1 = self.model.get_embedding(text1)
        embedding2 = self.model.get_embedding(text2)
        self.assertFalse(np.array_equal(embedding1, embedding2))


if __name__ == "__main__":
    unittest.main()
