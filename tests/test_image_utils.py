import unittest
from src.image_utils import load_image_from_path, load_image_from_url

class TestImageUtils(unittest.TestCase):
    def test_load_image_from_path(self):
        image = load_image_from_path("images/two-cats.jpg")
        self.assertIsNotNone(image)

    def test_load_image_from_url(self):
        image = load_image_from_url("http://images.cocodataset.org/val2017/000000039769.jpg")
        self.assertIsNotNone(image)

if __name__ == "__main__":
    unittest.main()
