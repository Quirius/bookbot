def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def count_words(text):
    return len(text.split())