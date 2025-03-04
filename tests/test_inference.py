import unittest
from PIL import Image
from src.inference import VQAInference

class TestVQAInference(unittest.TestCase):
    def setUp(self):
        self.vqa_inference = VQAInference(model_path="vqa")
        self.image = Image.new('RGB', (100, 100))

    def test_predict(self):
        question = "What is in the image?"
        answer = self.vqa_inference.predict(self.image, question)
        self.assertIsInstance(answer, str)

if __name__ == "__main__":
    unittest.main()
