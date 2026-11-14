
"""Text helpers. The worked example every contribution is modelled on."""


def word_count(text):
    """Count whitespace-separated words."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix


# Helper Function 1
def reverse_text(text):
    """Reverse the given text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text[::-1]


# Helper Function 2
def capitalize_words(text):
    """Capitalize the first letter of each word."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.title()


# Helper Function 3
def remove_extra_spaces(text):
    """Remove extra spaces from text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())
