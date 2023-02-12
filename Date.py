month_day_dct = {1: 31, 2: 28, 3: 31,
                 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30,
                 10: 31, 11: 30, 12: 31}


class Date:
    def __init__(self, month=1, day=1):
        self.__month = month
        self.__day = day

    def set_month(self, month):
        self.__month = month

    def set_day(self, day):
        self.__day = day

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def days_in_month(self):
        if self.__month in {4, 6, 9, 11}:
            return 30
        elif self.__month == 2:
            return 28
        else:
            return 31

    def advance(self):
        self.__day += 1
        if self.__day > self.days_in_month():
            self.__month += 1
            self.__day = 1

    def absolute_day(self):
        month_day = 0
        num_days = 0
        for i in range(1, 13):
            month_day += month_day_dct[i]
            if self.__month == i + 1:
                num_days = month_day + self.get_day()
                break
            elif self.__month == i:
                num_days = month_day
                break
        return num_days

    def from_absolute_day(self, absday):
        total_days = 0
        day = 0
        month = 0
        for i in range(1, 13):
            total_days += month_day_dct[i]
            if total_days >= absday:
                if absday == total_days:
                    day = month_day_dct[i]
                    month = i
                    break
                elif i == 1:
                    day = absday
                    month = i + 1
                    break
                else:
                    day = absday % month_day_dct[i - 1]
                    month = i
                    break

        return f'({month}, {day})'

    def shift(self, days):
        absday = self.absolute_day()
        total_days = absday + days
        return self.from_absolute_day(total_days)

    def __str__(self):
        return str(self.__month) + "/" + str(self.__day)

    def __eq__(self, other):
        return self.__month == other.__month and self.__day == other.__day
