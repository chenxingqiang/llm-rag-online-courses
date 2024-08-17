from transformers import AutoTokenizer, AutoModel
import torch


class EmbeddingModel:
    def __init__(self, model_name="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def get_embedding(self, text):
        inputs = self.tokenizer(
            text, return_tensors="pt", padding=True, truncation=True
        )
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()


# Usage example
if __name__ == "__main__":
    embedding_model = EmbeddingModel()
    text = "Hello, world!"
    embedding = embedding_model.get_embedding(text)
    print(f"Embedding shape: {embedding.shape}")
