def number_of_words(book):
    words = book.split()
    words_count = len(words)
    return words_count

def number_of_chars(book):
    unique_chars = set()
    dictionary = {}
    book_in_lowercase = book.lower()
    
    for c in book_in_lowercase:
        if c not in unique_chars:
            unique_chars.add(c)
            dictionary[c] = 1
        else:
            dictionary[c] += 1
    return dictionary

def sorted_list(dictionary):
    list = []

    def sort_on(dict):
        return dict["num"]

    for char in dictionary:
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = dictionary[char]

        list.append(char_dict)

    list.sort(reverse=True, key=sort_on)
    return list


