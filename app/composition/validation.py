FALLBACK_CONTENT = {
    "teaserQuestion": "Do you know why this movie stayed in the conversation for so long?",
    "funFactAnswer": (
        "It earned attention for its distinctive style and the way audiences kept talking about it afterward."
    ),
    "whyWatchNow": "A strong choice if you want something engaging tonight.",
    "hook": None,
}


def validate_composed_response(payload: dict) -> dict:
    engagement = payload["engagement"]
    required_fields = ["teaserQuestion", "funFactAnswer", "whyWatchNow"]
    if any(not isinstance(engagement.get(field), str) or not engagement.get(field) for field in required_fields):
        payload["engagement"] = FALLBACK_CONTENT
        payload["metadata"]["fallbackUsed"] = True
        return payload

    if engagement["teaserQuestion"] == engagement["funFactAnswer"]:
        payload["engagement"] = FALLBACK_CONTENT
        payload["metadata"]["fallbackUsed"] = True

    return payload
