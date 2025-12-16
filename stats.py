def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if not char.isalpha():
            continue
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_characters(char_count):
    def get_num(item):
        return item["num"]

    list_of_dicts = [{"char": char, "num": count} for char, count in char_count.items()]
    list_of_dicts.sort(key=get_num, reverse=True)
    return list_of_dicts

