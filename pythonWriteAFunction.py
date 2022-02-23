def is_leap(year):
    leap = False

    isDivisibleBy4 = year % 4 == 0
    isDivisibleBy100 = year % 100 == 0
    isDivisibleBy400 = year % 400 == 0

    if isDivisibleBy4:
        leap = True
        if isDivisibleBy100:
            leap = False
            if isDivisibleBy400:
                leap = True

    return leap


if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
