import re

def linkify(text: str):
    if text.count("http") != 0:
        return re.sub(r"(https?://[^\s]+)", lambda m: f"<a href=\"{m.group(0)}\">{m.group(0)}</a>", text)

# Example usage
text = "Check out this link: https://example.com and this one too: http://another.com"
result = linkify(text)
print(result)
