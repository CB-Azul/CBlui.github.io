def find_largest_num(num_list):
    largest_num = 0
    lowest_num = 0
    for num in num_list:
        if num>largest_num:
            largest_num=num
        if lowest_num==0 and lowest_num!=num:
            lowest_num = num
        elif num<lowest_num:
            lowest_num=num
    return lowest_num, largest_num


number = [11, 15, 34, 26, 8, 60, 75]
num_min, num_max = find_largest_num(number)
print(num_min, num_max)