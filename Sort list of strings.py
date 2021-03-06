from collections import OrderedDict

#Splitting the elements of the list
def split_list(list1):
    spt_char = list()
    for i in range(len(list1)):
        # list_spt = list()
        # list_spt.append(list1[i].split("."))
        spt_char.append(list1[i].split("."))
    print(spt_char)
    return spt_char

#Creating a list of length of all the elements of the list
def length_list(spt_char):
    list_len = list()
    for i in range(len(spt_char)):
        list_len.append(len(spt_char[i]))
    print(list_len)
    return list_len

list1 = ["1.0.0","1","1.1.0","1.1","1.0","1.1.1","1.1.1.0"]
s = split_list(list1)
l = length_list(s)

#defining the range of keys for the dictionary
dict_key_max_len = len(max(s, key=len))
for i in range(len(s)):
    while (len(s[i]) < dict_key_max_len):
        s[i].append('0')

dict_key = list(range(0, dict_key_max_len))

#creating a dictionary with none value
keys = {k:None for k in dict_key}

#Creating a dictionary with all the components of elements of a list and lengths of the elements
dict = OrderedDict()
i=0
for key in keys:
    for element in s:
        dict.setdefault(key, []).append(element[i])
    i += 1
dict['element_length'] = l

#Sorting is pending
OrderedDict(sorted(dict.items(), key=lambda t: t[0]))
#giving the following error: '<' not supported between instances of 'str' and 'int'
#tried a couple of other things but still giving the same error