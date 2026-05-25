def calc_median_temperature():
    user_input = input("Enter numbers separated by commas: ")

    string_list = user_input.split(",")

    temp_list = []
    for num in string_list:
        temp_list.append(float(num))

    sorted_list = sorted(temp_list)
    n = len(sorted_list)

    if n % 2 == 1:   # odd number of values
        median = sorted_list[n // 2]
    else:   # even number of values
        middle1 = sorted_list[n // 2 - 1]
        middle2 = sorted_list[n // 2]
        median = (middle1 + middle2) / 2

    print("Sorted List =", sorted_list)
    print("Median =", median)


calc_median_temperature()