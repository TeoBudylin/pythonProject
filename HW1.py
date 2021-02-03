print("Hello world !")

# a = input("Pls enter a: ")
#
# print(a)
# print(type(a))

s = input("Pls, enter time in seconds:  ")

ss = int(s) % 60

mm = int(s) // 60

hh = int(s) // 3600

if ss < 10:
    sss = "0"

print(f"{hh}:{mm}:{ss}")

