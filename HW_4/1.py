from sys import argv

zp = int(argv[1]) * int(argv[2]) + int(argv[3])

print(f"Зарплата сотрудника, работашего {int(argv[1])} часов со ставкой {int(argv[2])} рублей в час и премией {int(argv[3])} \
    составляет {zp} рублей")