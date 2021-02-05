s = input("Pls, enter time in seconds:  ")

hh = int(s) // 3600

mm = int(s) // 60 - hh * 60

ss = int(s) % 60

print(f"{hh:02}:{mm:02}:{ss:02}")