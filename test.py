def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
path_to_file = "books/frankenstein.txt"

def count_words (string):
    split_string = string.split()
    return len(split_string)
       

def count_characters (string):
    frank_dic={}

    for n in string:
        n=n.lower()
        if n not in frank_dic:
            frank_dic[n] = 1
        else:
            frank_dic[n] += 1

    return frank_dic











        



string = get_book_text(path_to_file)
num_words = count_words(string)
dic_of_char= count_characters(string)

list_of_dic = []
for letter in dic_of_char:
    count = dic_of_char[letter]
    list_of_dic.append( {"letter": letter, "count": count})

def sort_on(items):
    return items["count"]

def chars_to_sorted_list(dic_of_char):  
    list_of_dic = []
    for letter in dic_of_char:  
        count = dic_of_char[letter]
        if letter.isalpha():
            list_of_dic.append( {"letter": letter, "count": count}) 
        else:
            continue
    list_of_dic.sort(reverse=True, key=sort_on)
    return(list_of_dic) 
print (chars_to_sorted_list(dic_of_char))
