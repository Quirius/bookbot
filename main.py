import sys
from stats import count_words, get_book_text, count_characters, sort_characters

def main():
    if len(sys.argv) != 2:
        filepath = input("Enter the path to the book file: ")
    else:
        filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars = sort_characters(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
