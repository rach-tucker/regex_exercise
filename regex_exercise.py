import re

file = open("regex_test.txt")

data = file.readlines()

def is_name(list_names):

    pattern_name = re.compile('([A-Z][a-z]*) *([A-Z][a-z]*) *([A-Z][a-z]*)*')
    for d in list_names:
        if pattern_name.match(d):
            print(d)
        else:
            print("None")
is_name(data)
file.close()