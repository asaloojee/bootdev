def count_words(book):
    words = book.split()
    words = len(words)
    return words


def count_letters(book: str) -> dict[str, int]:
    letter_count = {}
    for char in book:
        char = char.lower()
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
    return letter_count


def sort_on(letter_pair: tuple[str, int]) -> int:
    return letter_pair[1]


def chars_dict_to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    chars = list()
    for key in char_dict:
        value = char_dict[key]
        count_tuple = (key, value)
        chars.append(count_tuple)
    sorted_chars = sorted(chars, reverse=True, key=sort_on)
    return sorted_chars
