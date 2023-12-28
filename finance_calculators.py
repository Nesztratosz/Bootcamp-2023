"""
1 need a line out with the options
2 choose the pathway
3 if Error
    print out a nice message that maybe they misspelled the word
4 if investment
    ask for Deposit
    Percentage (we divide with 100)
    Time
    is it simple
        use the correct calculating method for simple
            A = Deposit * (1 + Rate * Time)
    or compound
        use to correct calculating method for compound
            A = Deposit * math.pow(( 1 + Percent ),t)
    Print out the investment how much they earn in how many years with that many percentage
5 If Bond
    ask for Present value
    Interest rate (divide by 100 then 12)
    Monthly repay
    Then use the correct repayment calculation
        repayment = ( i * P ) / ( 1 - ( 1 + i ) ** (-n))
    Print out how much they need to pay back in that amount of time in month
"""

import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

print("Enter either 'investment' or 'bond' from the menu above to proceed: ")
choice = input("PLease give me what would you like to do: ").lower() #lowering the string so you wont have problem with
                                                                    #capitalize or capital letters

#making variables to make it easier in the process of deciding what would you like to do
bond = str("bond")
invest = str("investment")

if choice == bond:                #This will be the part that when you choose bond and counting out the result
    print("you chosen the bond option")
    value = int(input("Could you give me your House value: "))
    interest =int(input("Could you give me your interest rate: "))/100/12
    monthly= int(input("How many month would you like to sign up? "))
    repay = ( interest * value ) / ( 1 - ( 1 + interest ) ** (-monthly))
    rep = float(round(repay,2))     # didnt manage to put together f string with round
    print(f"That how much {rep} you have to pay monthly")

elif choice == invest:                                      # This would be the part when you choose investing
    print("you chosen the option investment")
    deposit = int(input("PLease give me the amount of deposit you would like to invest: "))
    percentage = int(input("Please provide the percentage they give to you: "))/100
    time = int(input("PLease provide the length of time in years: "))
    simple = str("simple")
    compound = str("compound")
    choice2 = input("PLease give me if you looking for 'simple' or 'compound' investment ").lower()
    # from here it will go to simple and compound calculating

    if choice2 == simple:                                               #A = Deposit * (1 + Percent * Time)
        print("you chose simple investment: ")
        amount_simple = deposit * (1 + percentage * time)
        print(f"You will have {amount_simple} money after the simple investment, with the information you given")

    elif choice2 == compound:                                           #A = Deposit * math.pow(( 1 + Percent ),t)
        print("you choose coumpound investment")
        a = deposit * math.pow ( ( 1 + percentage ) , time )
        amount_compound = float(round(a,2))                         # didnt manage to put together f string with round
        print(f"You will have {amount_compound} after the compound investment")

    else :
        print("You might have misspelled the word please check it")

else :
    print("You might have misspelled the word please check it")
