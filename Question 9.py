def days_since_birthday(birthday):

    day, month, year = map(int, birthday.split('-'))


    current_day = 26
    current_month = 2
    current_year = 2024


    days_difference = 0


    for m in range(1, month):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            days_difference += 31
        elif m in [4, 6, 9, 11]:
            days_difference += 30
        else:
            days_difference += 28

    days_difference += day - 1


    for m in range(1, current_month):
        if m in [1, 3, 5, 7, 8, 10, 12]:
            days_difference += 31
        elif m in [4, 6, 9, 11]:
            days_difference += 30
        else:
            days_difference += 28

    days_difference += current_day - 1

    for y in range(year + 1, current_year):
        days_difference += 365

    return days_difference

birthday_string = "03-04-2005"
result = days_since_birthday(birthday_string)
print(f"Days since {birthday_string}: {result} days")

