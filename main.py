def main():
    frankenstein = "books/frankenstein.txt"
    
    with open(frankenstein) as f:
        file_contents = f.read()

    print(f"{count_words(file_contents)} words found in this document")

def count_words(text):
    words = text.split()
    
    return len(words)


main()