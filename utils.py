def capitalize_words(string):
    words = string.split()
    capitalized_words = [word.capitalize() if not any(char.isdigit() for char in word) else word for word in words]
    return ' '.join(capitalized_words)