
# fibonnaci = 0
def generate_fibonnaci(num):
    num1 = 0
    num2 = 1
    #answer = [num1, num2]
    answer = []
    for i in range(num-2):
        # print(num1)

        fibonnacci = num1 + num2
        #print(num1, num2, fibonnacci)
        num1 = num2
        num2 = fibonnacci

        answer.append(fibonnacci)
    return answer
    answer = None
    print("hello")


num = int(input("Input number of fibonnaci sequence:"))
answer = generate_fibonnaci(num)
print(answer)





#     0
#     1
# 0 + 1 = 1
# 1 + 1 = 2
# 1 + 2 = 3
# 3 + 2 = 5
# 5 + 3 = 8
# 8 + 5 = 13
#
# 5