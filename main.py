import sys

from stats import sorted_list
from stats import number_of_chars
from stats import number_of_words

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = number_of_words(book)
    char_dictionary = number_of_chars(book)
    list = sorted_list(char_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    for dictionary in list:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END =============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
elif len(sys.argv) == 2:
    main()
