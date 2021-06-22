import os
import re

lists = os.listdir()
print(lists)




for list in lists:
    if list.endswith('.txt'):
        with open(list, 'r') as file:
            lines = file.readlines()

        with open(list, 'w') as file:
            for line in lines:
                # find() returns -1 if no match is found
                if line[:4].find("4 ") != -1:
                    pass
                else:
                    file.write(line)
