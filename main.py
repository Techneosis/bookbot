def character_count(book_text: str) -> dict[str, int]:
    ret: dict[str, int] = {}
    book_text = book_text.lower()
    for c in book_text:
        ret[c] = ret.get(c, 0) + 1

    return ret


def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{len(file_contents.split())} words found in the document")
        print("")
        c_counts = character_count(file_contents)
        for k in c_counts:
            print(f"The '{k}' character was found {c_counts[k]} times")


main()
