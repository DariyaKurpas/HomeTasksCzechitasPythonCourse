from dateutil.parser import parse

just_time = parse("2021.02.21 on Monday at 07:41")
print(just_time)


just_time = parse("On 21-02-2021 on Monday at 15:12")
print(just_time)


# just_time = parse("2021.02.21 on Monday at 07:41")
# print(just_time)


# just_time = parse("2021.02.21 on Monday at 07:41")
# print(just_time)