def histogram(string_list):
    string_dict = dict()
    for word in string_list:
        if word not in string_dict:
            string_dict[word] = 1
        else:
            string_dict[word] += 1
    print(string_dict)

lst = ['word','text','word','word','string']
histogram(lst)