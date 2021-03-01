class MyZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt

try:
    a = 1 / 0

except ZeroDivisionError:
    print("Делить на нуль нельзя!")

finally:
    print("конец программы")
