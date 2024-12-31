from transformers import pipeline

def init_hate_speech_pipeline():
    return pipeline("text-classification", model="monologg/koelectra-base-v3-hate-speech")

def detect_hate_speech(text, pipe, chunk_size=512):
    results = []
    for start in range(0, len(text), chunk_size):
        chunk = text[start:start+chunk_size]
        chunk_result = pipe(chunk, truncation=True, max_length=chunk_size)
        results.extend(chunk_result)

    for res in results:
        label = res["label"].lower()
        if label in ["hate", "offensive"]:
            return label
    return "none"
