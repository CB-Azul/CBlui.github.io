# def atm_withdraw(withdraw):
#     thou = withdraw//1000
#     fivehun = (withdraw%1000)//500
#     twohun = ((withdraw%1000)%500)//200
#     onehun = (((withdraw%1000)%500)%200)//100
#
#     if withdraw // 1000 >= 1 and (withdraw % 1000 >= 100 or withdraw % 1000 == 0):
#             print("P1000 x", thou)
#     else:
#         print("Invalid Amount!")
#     if (withdraw%1000)//500 >= 1 and (withdraw % 1000 >= 100 or withdraw % 1000 == 0):
#             print("P500 x", fivehun)
#     else:
#         pass
#     if ((withdraw%1000)%500)//200 >= 1:
#             print("P200 x", twohun)
#     else:
#         pass
#     if (((withdraw%1000)%500)%200)//100 >= 1:
#             print("P100 x", onehun)
#     else:
#         pass
#
# withdraw = int(input("Withdraw amount: P"))
# atm_withdraw(withdraw)

def atm_withdraw(withdraw_amount):
    thou = withdraw//1000
    fivehun = (withdraw%1000)//500
    twohun = ((withdraw%1000)%500)//200
    onehun = (((withdraw%1000)%500)%200)//100
    invalid = (((withdraw%1000)%500)%200)


    if thou>=1 and ((invalid == 500 or invalid ==200 or invalid==100) or invalid == 0):
        print("P1000 x", thou)
        if withdraw%1000 <= 999 and fivehun>=1:
            print("P500 x", fivehun)
        if (withdraw%1000)%500 <=499 and twohun>=1:
            print("P200 x", twohun)
        if invalid <=199 and onehun >= 1:
            print("P100 x", onehun)
    elif fivehun>=1 and ((invalid ==200 or invalid==100) or invalid == 0):
        print("P500 x", fivehun)
        if invalid <=499 and twohun>=1:
            print("P200 x", twohun)
        if invalid <=199 and onehun >= 1:
            print("P100 x", onehun)
    elif twohun>=1 and (invalid ==100 or invalid == 0):
        print("P200 x", twohun)
        if invalid <=199 and onehun >=1:
            print("P100 x", onehun)
    elif onehun>=1 and invalid <= 100:
        print("P100 x", onehun)
    else:
        print("Invalid Amount!")
        return withdraw

withdraw = int(input("Withdraw amount: P"))
atm_withdraw(withdraw)
#print(result)