
def generate_num_bits(num_of_bits):
    list_of_bits = []
    for x in range(0, num_of_bits):
        binary_value = 2 ** x
        print("2^" + str(x) + " = " + str(binary_value))
        list_of_bits.append("2^" + str(x) + " = " + str(binary_value))
    return list_of_bits


num_of_bits = int(input("Input the number of bits:\n"))
answer = generate_num_bits(num_of_bits)
print(answer)

#trial for git testing
#testing for git status short
#adding line for git branch merge
#added line for branch merge