def is_leap_year(lower_range, higher_range):
    lower_range = int(lower_range) - 1
    higher_range = int(higher_range)
    range_list = []
    while lower_range < higher_range:
        lower_range = lower_range + 1
        if lower_range % 4 == 0 and lower_range % 100 != 0:
            range_list.append(lower_range)

        elif lower_range % 4 == 0 and lower_range % 100 == 0:
            if lower_range % 100 == 0 and lower_range % 400 != 0:
                pass
            else:
                range_list.append(lower_range)
        else:
            pass
    return range_list


print(is_leap_year(1900, 1920))

# print(type(is_leap_year(1900, 1920)))
#
# usageExample = (is_leap_year(1900, 1920))
# for leapYear in usageExample:
#     print(leapYear)
