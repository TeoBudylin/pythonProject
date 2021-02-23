import re

dict = {}

with open("text_6.txt", encoding="utf-8", mode="r") as f:
    for line in f:
        predmet, stats = line.split(":")
        words = re.findall(r'\w+', stats)
        ours = 0
        for word in words:
            if (word.isnumeric() == True):
                ours += int(word)
        dict[predmet] = ours

print(dict)