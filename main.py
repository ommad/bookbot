def main():

    book_path = ".\\books\\frankenstein.txt"

    book_text = open_book(book_path)

    word_count = count_words(book_text)

    letter_count = count_letters(book_text)

    # Display book statistics
    print(f"--- Book statistic for {book_path} ---")
    print(f"Book contains {word_count} words.")
    print("Here is the letter count:")
    display_letter_count(letter_count)
    print(f"--- End of the report ---")

# Receives a book as string and counts the number of words
def count_words(book_text) :
    words = book_text.split()
    return len(words)

# Receives a filesystem path, opens it and sends it back its content as a string
def open_book(book_path) :
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def count_letters(book_text) :
    letter_count = {}

    lower_char_book = book_text.lower()

    for character in lower_char_book :
        if character in letter_count: letter_count[character] += 1
        else : letter_count[character] = 1
    
    return letter_count

def sort_on_letter_count(letter):
    return letter["count"]

def display_letter_count(letter_count) :

    letter_list = []

    for letter in letter_count:
        if letter.isalpha() :
            letter_list.append(
                {"letter" : letter,
                "count" : letter_count[letter]}
            )
    letter_list.sort(reverse=True, key=sort_on_letter_count)
    
    for letter in letter_list:
        print(f"The '{letter["letter"]}' character was found {letter["count"]} times.")

main()