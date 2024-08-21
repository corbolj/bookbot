def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_letters(text)
    sorted_list = sorter(letter_count)
    for line in sorted_list:
        print(f"The '{line['letter']}' character was found {line['count']} times")

def sort_on(dict):
    return dict['count']

def sorter(letter_count):
    list_of_dict = []
    for entry in letter_count:
        if entry.isalpha():
            list_of_dict.append({'letter': entry, 'count': letter_count[entry]})
        list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def count_letters(text):
    letter_count = dict()
    for letter in text:
        letter = letter.lower()
        if letter in letter_count:
            count = letter_count[letter]
            count += 1
        else:
            count = 1
        letter_count[letter] = count
    return letter_count

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
