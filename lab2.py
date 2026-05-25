def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    user_input = input()
    string_list = user_input.split(",")
    float_list = []
    for num in string_list:
        float_list.append(float(num))
    return float_list


def calc_average(temp_list):
    return (sum(temp_list) / len(temp_list))

    
def find_min_max(temp_list):
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    return [min_temp, max_temp]

def sort_temperature(temp_list):
    sorted_list = sorted(temp_list)

def calc_median_temperature(temp_list):
    sorted_list = sorted(temp_list)
    n = len(sorted_list)

    if n % 2 == 1:   # odd number of items
        return sorted_list[n // 2]

    else:   # even number of items
        middle1 = sorted_list[n // 2 - 1]
        middle2 = sorted_list[n // 2]
        return (middle1 + middle2) / 2
    
def main():
    display_main_menu()

    num_list = get_user_input()

    avg = calc_average(num_list)
    min_max = find_min_max(num_list)
    sorted_list = sort_temperature(num_list)
    median = calc_median_temperature(num_list)

    print("Average =", avg)
    print("Minimum =", min_max[0])
    print("Maximum =", min_max[1])
    print("Sorted List =", sorted_list)
    print("Median =", median)


if __name__ == "__main__":
    main()
