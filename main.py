def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

main()
