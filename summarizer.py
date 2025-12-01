from utils import clean_text
from model_stub import predict_summary

def summarize(text: str) -> str:
    cleaned = clean_text(text)
    return predict_summary(cleaned)
