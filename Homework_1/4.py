num_srt = input("Pls, enter your number:  ")

num = int(num_srt)

max_digit = 0

while num != 0:
    if (num % 10 > max_digit):
        max_digit = num % 10
    num = num // 10

print(f"максимальная цифра: {max_digit}")
