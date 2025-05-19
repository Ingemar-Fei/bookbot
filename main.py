import stats
import sys

def get_book_text(path_to_file:str):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
    return file_contents

def print_report(path_to_file):
    contents = get_book_text(path_to_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    num_words = stats.get_num_words(contents)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    dict_num_words = stats.get_num_characters(contents)
    list_num_words = stats.sort_num_characters(dict_num_words)
    for i in list_num_words:
        print(f"{i["name"]}: {i["num"]}")
    print("============= END ===============")
    return 0
def main():
    if len(sys.argv) > 1:
        print_report(path_to_file=sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
main()