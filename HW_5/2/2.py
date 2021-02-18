with open("text_2.txt", "r") as f:
    lines = f.readlines()
    print(lines)

print(f"Количество строк в файле - {len(lines)}")

for i in range(0, len(lines)):
    print(f"Количество слов в строке {i + 1} - {lines[i].count(' ') + 1}")