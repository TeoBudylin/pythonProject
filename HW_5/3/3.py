persons = 0
total_salary = 0

with open("text_3.txt", "r") as f:
        for line in f:
            # print(line)
            surname = line.split()[0]
            salary = int(line.split()[1])
            if (salary < 20000):
                print(f"{surname}'s salary is less then 20000 rubles")
            persons += 1
            total_salary += salary

print(f"Среднее арифметическое зарплаты составляет {total_salary / persons}")