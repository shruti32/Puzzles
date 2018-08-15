# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 17:32:33 2018

@author: shrut
"""
list1 = ["1.0.0","1","1.1.0","1.1","1.0","1.1.1","1.1.1.0"]
def length_list(list1):
    list_len = list()
    for i in range(len(list1)):
        list_len.append(len(list1[i]))
        print(list_len)
    return length_list
print(length_list(list1))

spt_char = list()
def split_list(list1):
    for i in range(len(list1)):
        list_spt = list()
        list_spt.append(list1[i].split("."))
        spt_char.append(list_spt)
        print(spt_char)
    return split_list
print(split_list(list1))

list2 = spt_char
print(list2)




