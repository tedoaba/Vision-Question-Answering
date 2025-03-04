import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from src.image_utils import load_image_from_path, load_image_from_url
from src.inference import VQAInference

def main():
    parser = argparse.ArgumentParser(description="Visual Question Answering System")
    parser.add_argument("--image", type=str, required=True, help="Path or URL of the image")
    parser.add_argument("--question", type=str, required=True, help="Question about the image")
    parser.add_argument("--url", action="store_true", help="Set this flag if the image is a URL")
    parser.add_argument("--model_path", type=str, default=None, help="Path to local model directory")

    args = parser.parse_args()

    # Load image
    if args.url:
        image = load_image_from_url(args.image)
    else:
        image = load_image_from_path(args.image)

    # Run inference
    vqa = VQAInference(model_path=args.model_path)
    answer = vqa.predict(image, args.question)

    print("\n🖼️  Image:", args.image)
    print("❓ Question:", args.question)
    print("✅ Predicted Answer:", answer)

if __name__ == "__main__":
    main()
