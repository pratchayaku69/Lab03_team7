def reverse_words(text):
    """Reverse the order of words in text, ignoring extra whitespace."""
    return " ".join(text.split()[::-1])
