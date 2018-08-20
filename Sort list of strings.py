# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 17:32:33 2018

@author: shrut
"""
list1 = ["1.0.0","1","1.1.0","1.1","1.0","1.1.1","1.1.1.0"]

list_len = list()
def length_list(list1):
    for i in range(len(list1)):
        list_len.append(len(list1[i]))
        print(list_len)
    return length_list
print(length_list(list1))

print(list_len)

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

list_sorted = list()
def sorted_string(list2, list1, list_len):
    for i in range(len(list2)):
        for j in range(i+1, len(list2)):
            #two while loops to make strings equal in length
            while(len(list2[i])<len(list2[j])):
                list2[i].append('0')
                print(list2)
            while(len(list2[i])>len(list2[j])):
                list2[j].append('0')
                #sort the strings
            if(list2[i][0:len(list2[i])]<list2[j][0:len(list2[j])]):
                list_sorted.append(list1[i])
                #we will compare the characters at each position and at the instant the
                #character of one string is greater than other we will assign that element first place
            elif(list2[i][0:len(list2[i])]==list2[j][0:len(list2[j])]):
                if(list_len[i]<list_len[j]):
                    list_sorted.append(list1[i])
                else:
                    list_sorted.append(list1[j])
                list_sorted.append(list1[i])#this will go a long way, I need your guidance here
    return sorted_string

print(sorted_string(list2, list1))