# app/classifier.py

def classify_intent(message: str) -> str:
    message = message.lower()

    if "pipeline" in message or "deploy" in message:
        return "ci_cd"
    elif "launch" in message or "instance" in message:
        return "instance_creation"
    elif "cpu" in message or "usage" in message:
        return "monitoring"
    elif "log" in message:
        return "logs"
    elif "volume" in message or "storage" in message:
        return "storage"
    else:
        return "unknown"