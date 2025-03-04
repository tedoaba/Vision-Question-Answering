from transformers import ViltProcessor, ViltForQuestionAnswering
import os

class VQAModel:
    """Handles loading the VQA model and processor, either from Hugging Face or a local directory."""
    
    def __init__(self, model_path=None):
        """
        Initialize the VQA model.
        
        :param model_path: Optional local directory path to load the model from.
        """
        if model_path and os.path.exists(model_path):
            print(f"🔹 Loading model from local directory: {model_path}")
            self.processor = ViltProcessor.from_pretrained(model_path)
            self.model = ViltForQuestionAnswering.from_pretrained(model_path)
        else:
            print("🌍 Loading pre-trained model from Hugging Face")
            self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
            self.model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    def get_processor(self):
        return self.processor

    def get_model(self):
        return self.model
