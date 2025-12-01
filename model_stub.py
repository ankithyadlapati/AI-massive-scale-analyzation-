def predict_summary(cleaned_text: str) -> str:
    words = cleaned_text.split()
    if len(words) <= 10:
        return cleaned_text
    return " ".join(words[:10]) + " ..."
