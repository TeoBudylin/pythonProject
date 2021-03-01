class Date:
    day = 0
    month = 0
    year = 0
    def __init__(self,date):
        self.date = date

    @classmethod
    def transf(cls, date):
        day, month, year = map(int, date.split("-"))
        return [day, month, year]

    @staticmethod
    def validate(day, month, year):
        if day <= 31 and month <= 12:
            return True
        else:
            return False


#date = Date("31-12-1987")

print(Date.transf("31-12-1987"))

print(Date.validate(31, 14, 1990))