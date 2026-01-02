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

def sort_on(items):
    return items["num"]

def chars_to_sorted_list(dic_of_char):  
    list_of_dic = []
    for char in dic_of_char:  
        num = dic_of_char[char]
        if char.isalpha():
            list_of_dic.append( {"char": char, "num": num}) 
    list_of_dic.sort(reverse=True, key=sort_on)
    return (list_of_dic)
