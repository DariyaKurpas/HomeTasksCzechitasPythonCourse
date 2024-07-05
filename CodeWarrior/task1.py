def difference_in_ages(ages):
    minimum_age = 999
    maximum_age = 0
    for number in ages:
        if number < minimum_age:
            minimum_age = number
    for number in ages:
        if number > maximum_age:
            maximum_age = number
    age_difference = maximum_age - minimum_age
    return minimum_age, maximum_age, age_difference

print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))
