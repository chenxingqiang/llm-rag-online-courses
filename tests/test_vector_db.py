import unittest
import numpy as np
from src.vector_db.vector_db import VectorDB


class TestVectorDB(unittest.TestCase):
    def setUp(self):
        self.db = VectorDB()
        self.db.add_document("Document 1", np.array([1, 0, 0]))
        self.db.add_document("Document 2", np.array([0, 1, 0]))
        self.db.add_document("Document 3", np.array([0, 0, 1]))

    def test_add_document(self):
        self.assertEqual(len(self.db.documents), 3)
        self.assertEqual(len(self.db.embeddings), 3)

    def test_search(self):
        query_embedding = np.array([1, 0, 0])
        results = self.db.search(query_embedding, top_k=2)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], "Document 1")

    def test_empty_db_search(self):
        empty_db = VectorDB()
        results = empty_db.search(np.array([1, 0, 0]))
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
