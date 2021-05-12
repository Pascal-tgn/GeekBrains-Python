class Data:
    plainText: str
    dd: int
    mm: int
    yyyy: int

    def __init__(self, inputData: str):
        self.plainText = inputData
        self.dd, self.mm, self.yyyy = self.to_int(self)
        self.validate(self)

    @classmethod
    def to_int(cls, dateValue: str):
        dd, mm, yyyy = dateValue.plainText.split('-')
        return int(dd), int(mm), int(yyyy)

    @staticmethod
    def validate(data):
        dd, mm, yyyy = Data.to_int(data)
        if dd < 1 or dd > 31 or mm < 1 or mm > 12 or yyyy < 1000 or yyyy > 2021:
            print('Date error. Please enter it in format DD-MM-YYYY with dashes.')
        else:
            print('Date format is OK.')


dt1 = Data('11-05-2020')
dt2 = Data('111-222-333')
print(f"dt1 day = {dt1.dd}, month = {dt1.mm}, year = {dt1.yyyy}")
