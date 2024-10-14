def capitalize_words(string):
    # Split the string into words
    words = string.split()

    # Capitalize each word if it doesn't contain a digit
    capitalized_words = [word.capitalize() if not any(char.isdigit() for char in word) else word for word in words]

    # Join the words back into a string and return
    return ' '.join(capitalized_words)