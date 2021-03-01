class myExeption(Exception):
    def __init__(self, txt):
        self.txt = txt

list =[]
while True:
    new_elem = input("Введите следующее число, для окончания вверидте STOP: ")
    if new_elem == "STOP":
        break
    try:
        list.append(int(new_elem))
    except Exception as e:
        print(e)


print(list)