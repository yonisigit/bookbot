from stats import get_num_chars, get_num_words, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sorted_char_count):
    print("============ BOOKBOT ============")  
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_char_count:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============= END ===============")




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    char_count = get_num_chars(book_text)
    sorted_char_count = sort_dict(char_count)
    print_report(book_path, word_count, sorted_char_count)
    


main()
    