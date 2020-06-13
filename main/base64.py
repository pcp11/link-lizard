import base64


def encode(message):
    message_bytes = message.encode("utf-8")
    encoded_bytes = base64.b64encode(message_bytes)
    return str(encoded_bytes, "utf-8")


def decode(base64_message):
    base64_bytes = base64.b64decode(base64_message)
    return str(base64_bytes, "utf-8")
