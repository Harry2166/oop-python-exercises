import random

names = open(r'/home/harry2166/Desktop/repos/oop-python-exercises/SocialNetwork/first-names.txt') # input your actual directory here
name_list = []
for line in names:
    name_list.append(line.strip())