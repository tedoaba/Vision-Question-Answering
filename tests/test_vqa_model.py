import unittest
from src.vqa_model import VQAModel

class TestVQAModel(unittest.TestCase):
    def test_load_model_from_huggingface(self):
        model = VQAModel()
        self.assertIsNotNone(model.get_processor())
        self.assertIsNotNone(model.get_model())

    def test_load_model_from_local_directory(self):
        model = VQAModel(model_path="vqa")
        self.assertIsNotNone(model.get_processor())
        self.assertIsNotNone(model.get_model())

if __name__ == "__main__":
    unittest.main()
