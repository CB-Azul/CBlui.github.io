# def sort_list(number, ascending=True):
#     sorted_number = sorted(number, reverse=not ascending)
#     return sorted_number
#
# ascending_order = sort_list(number, ascending=True)
# print(ascending_order)
#
# descending_order = sort_list(number, ascending=False)
# print(descending_order)




# def sort_asc_dec(number):
#     for w in range(0, len(number)):
#         for x in range(w+1, len(number)):
#             if number[w] >= number[x]:
#                 number[w], number[x] = number[x], number[w]
#         return  number

def sort_asc_dec(number):
    for x in range(0, len(number)):
        for y in range(x+1, len(number)):
            if number[x] <= number[y]:
                number[x], number[y] = number[y],number[x]
    return number


number = [11, 15, 34, 26, 8, 60, 75]
print(sort_asc_dec(number))


#[8, 11, 15, 26, 34, 60, 75]
#[11, 15, 34, 26, 8, 60, 75]