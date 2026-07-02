from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import torch
import re

MODEL_PATH = "model/best_distilbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

labels = {
    0: "☹ Negative",
    1: "😐 Neutral",
    2: "😊 Positive"
}


def predict_sentiment(text):

    inputs = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=512,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)

    prediction = torch.argmax(probs, dim=1).item()

    confidence = probs[0][prediction].item()

    return labels[prediction], confidence


def split_sentences(text):

    sentences = re.split(r"[.!?]+", text)

    return [s.strip() for s in sentences if s.strip()]