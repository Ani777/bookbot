import sys

from stats import get_num_words, get_book_text, count_characters, sort_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    number_of_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")

    characters = count_characters(text)
    sorted_characters = sort_characters(characters)
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character['num']}")
    print("============= END ===============")
main()