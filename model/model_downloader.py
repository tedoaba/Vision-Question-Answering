from transformers import ViltProcessor, ViltForQuestionAnswering

model_path = "vqa"
model_name = "dandelin/vilt-b32-finetuned-vqa"

processor = ViltProcessor.from_pretrained(model_name)
processor.save_pretrained(model_path)

model = ViltForQuestionAnswering.from_pretrained(model_name)
model.save_pretrained(model_path)

print("✅ Model downloaded and saved to:", model_path)
