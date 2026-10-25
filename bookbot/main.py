import sys
from stats import chars_dict_to_sorted_list, count_letters, count_words


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def print_report(path: str, word_count: int, sorted_chars: list[tuple[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        frankenstein = f.read()
    word_count = count_words(frankenstein)
    letters = count_letters(frankenstein)
    sorted_chars = chars_dict_to_sorted_list(letters)
    print_report(sys.argv[1], word_count, sorted_chars)


main()
