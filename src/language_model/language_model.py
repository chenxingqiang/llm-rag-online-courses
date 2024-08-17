from transformers import AutoTokenizer, AutoModelForCausalLM


class LanguageModel:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_text(self, prompt, max_length=50):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


# Usage example
if __name__ == "__main__":
    lm = LanguageModel()
    prompt = "The future of AI is"
    generated_text = lm.generate_text(prompt)
    print(f"Generated text: {generated_text}")
