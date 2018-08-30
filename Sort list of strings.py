# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 17:32:33 2018

@author: shrut
"""
def split_list(list1):
    spt_char = list()
    for i in range(len(list1)):
        # list_spt = list()
        # list_spt.append(list1[i].split("."))
        spt_char.append(list1[i].split("."))
    print(spt_char)
    return spt_char
#print(split_list(list1))
# print(spt_char)

def length_list(spt_char):
    list_len = list()
    for i in range(len(spt_char)):
        list_len.append(len(spt_char[i]))
    print(list_len)
    return list_len

list1 = ["1.0.0","1","1.1.0","1.1","1.0","1.1.1","1.1.1.0"]
s = split_list(list1)
l = length_list(s)

def sorted_string(s, l):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            #two while loops to make strings equal in length
            while(l[i]<l[j]):
                s[i].append('0')
            print(s)
            while(l[i]>l[j]):
                 s[j].append('0')
            print(s)
            #sort the strings
            # if(list2[i][0:len(list2[i])]<list2[j][0:len(list2[j])]):
            #     list_sorted.append(list1[i])
            #     #we will compare the characters at each position and at the instant the
            #     #character of one string is greater than other we will assign that element first place
            # elif(list2[i][0:len(list2[i])]==list2[j][0:len(list2[j])]):
            #     if(list_len[i]<list_len[j]):
            #         list_sorted.append(list1[i])
            #     else:
            #         list_sorted.append(list1[j])
            #     list_sorted.append(list1[i])#this will go a long way, I need your guidance here
    return s

# find the longest element in s and assign the number of keys in the dictionary to sort according to that
# Complete by today
