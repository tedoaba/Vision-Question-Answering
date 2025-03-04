import torch
from src.vqa_model import VQAModel

class VQAInference:
    """Runs inference on a given image-question pair using the VQA model."""
    
    def __init__(self, model_path=None):
        """
        Initialize the VQA inference pipeline.
        
        :param model_path: Optional local directory path to load the model from.
        """
        self.vqa = VQAModel(model_path=model_path)
        self.processor = self.vqa.get_processor()
        self.model = self.vqa.get_model()

    def predict(self, image, question):
        """Processes inputs and returns the predicted answer."""
        inputs = self.processor(image, question, return_tensors="pt")
        outputs = self.model(**inputs)
        predicted_class_idx = torch.argmax(outputs.logits, dim=-1).item()
        return self.model.config.id2label[predicted_class_idx]
