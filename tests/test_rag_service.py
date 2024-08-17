import unittest
from unittest.mock import MagicMock
from src.rag_service.rag_proxy_service import RAGProxyService


class TestRAGProxyService(unittest.TestCase):
    def setUp(self):
        self.rag_service = RAGProxyService()
        self.rag_service.embedding_model.get_embedding = MagicMock(
            return_value=[0.1, 0.2, 0.3]
        )
        self.rag_service.vector_db.search = MagicMock(
            return_value=["Relevant document 1", "Relevant document 2"]
        )
        self.rag_service.language_model.generate_text = MagicMock(
            return_value="Generated response"
        )

    def test_process_query(self):
        query = "What is the capital of France?"
        response = self.rag_service.process_query(query)

        self.rag_service.embedding_model.get_embedding.assert_called_once_with(query)
        self.rag_service.vector_db.search.assert_called_once()
        self.rag_service.language_model.generate_text.assert_called_once()

        self.assertEqual(response, "Generated response")


if __name__ == "__main__":
    unittest.main()
