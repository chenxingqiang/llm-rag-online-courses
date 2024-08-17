from src.embedding.embedding_model import EmbeddingModel
from src.language_model.language_model import LanguageModel
from src.vector_db.vector_db import VectorDB


class RAGProxyService:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.language_model = LanguageModel()
        self.vector_db = VectorDB()

    def process_query(self, query):
        # Get query embedding
        query_embedding = self.embedding_model.get_embedding(query)

        # Retrieve relevant documents
        relevant_docs = self.vector_db.search(query_embedding)

        # Prepare context
        context = "\n".join(relevant_docs)

        # Generate response
        prompt = f"Context: {context}\n\nQuery: {query}\nAnswer:"
        response = self.language_model.generate_text(prompt)

        return response


# Usage example
if __name__ == "__main__":
    rag_service = RAGProxyService()
    query = "What is the capital of France?"
    response = rag_service.process_query(query)
    print(f"Response: {response}")
