import sys
from stats import count_words, count_characters, chars_to_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
for arg in sys.argv:
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")     
        sys.exit(1)
    else:
        continue
path_to_file=sys.argv[1]
def main(): 
    string = get_book_text(path_to_file)
    num_words = count_words(string)
    dic_of_char= count_characters(string)
    updated_dic=chars_to_sorted_list(dic_of_char)

    print("============ BOOKBOT ============ \nAnalyzing book found at books/frankenstein.txt...\n"
    "----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in updated_dic:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

    print("============= END ===============")
    

main()

