from stats import get_num_chars, get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents




def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(f"{get_num_words(book_text)} words found in the document")
    book_char_nums = get_num_chars(book_text)
    print(book_char_nums)


main()
    