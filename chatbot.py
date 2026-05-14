import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "knowledge_base.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    KNOWLEDGE_BASE = json.load(f)

KEYWORDS = {
    "greeting": [
    "hello", "hi", "hey", "namaste",
    "हेलो", "नमस्ते"
],
    "emergency": [
        "emergency", "police", "ambulance",
        "आपात", "पुलिस"
    ],

    "hospital": [
        "hospital", "doctor",
        "अस्पताल", "डॉक्टर"
    ],

    "weather": [
        "weather", "rain",
        "मौसम", "बारिश"
    ],

    "tourism": [
        "tourism", "temple",
        "पर्यटन", "मंदिर"
    ]
}

def detect_topic(text):
    text = text.lower()

    for topic, keywords in KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return topic

    return None

def get_response(user_message, language="en"):
    topic = detect_topic(user_message)

    if topic and topic in KNOWLEDGE_BASE:
        lang_data = KNOWLEDGE_BASE[topic].get(language)

        if not lang_data:
            lang_data = KNOWLEDGE_BASE[topic]["en"]

        return lang_data["text"], lang_data["cards"]

    return (
        "Sorry, I didn't understand.",
        []
    )