def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document.\n")
    for char in chars_dict:
        print(f"The '{char['character']}' character was found {char['num']} times")
    print("--- End report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    
    char_list = []
    for char, count in chars.items():
        char_list.append({"character": char, "num": count})
    
    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list

def get_book_text(path):
    with open(path) as f:
        return f.read()





main()

