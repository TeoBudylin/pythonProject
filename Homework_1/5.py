proceeds = input("пожалуйта введите выручку")

cost = input("пожалуйта введите издержки")

if (int(proceeds) < int(cost)):
    print("фирма работает в убыток")
elif (int(proceeds) == int(cost)):
    print("выручка равна издержкам")
else: staff_num = input("пожалуйста, введите число сотрудников")
      prof = (int(proceeds) - int(cost)) / int(staff_num)
      print(f"рентабельность на одного сотрудника равна {prof}")
