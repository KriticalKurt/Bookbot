def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words are in this document. List of characters used below. \n{chars_dict}")
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    sorted_char = dict(sorted(chars.items()))
    return sorted_char
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()













