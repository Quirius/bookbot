from stats import count_words, get_book_text, count_characters, sort_characters

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars = sort_characters(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
