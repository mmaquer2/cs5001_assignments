'''
Michael Maquera
CS5002
HW 1
atm.py

FLOWCHART

start -> ask user for withdraw amount -> 
-> calculate the lowest amount of bank notes -> calculate the fifty bills by finding the modulo remainder
of fifty, then subract the number of bills from the requested amount -> and repeat this process for each of the bank notes
-> end



'''

def main():
    
    #get withdraw amount from user
    cash_withdraw = int(input('how much money are you taking out today? '))

    #calculate the lowest amount of bank notes
    
    #calculate number of 50 bills
    #find the modoulo remainder of the cash withdraw request of 50
    fifty_bills =cash_withdraw // 50

    #calculate the remaining cash from taking the product of the total number of 50 bills, and subtract that
    #from the total withdraw amount
    remaining_cost50 = cash_withdraw - (fifty_bills * 50)

    #calculate number of 20 bills
    #find the modulo remainder of the remaining cost subtracted from the 50 dollar calculation

    twenty_bills = remaining_cost50// 20

    #solve for remaining cash from 20's
    remaining_cost20 = remaining_cost50 - (twenty_bills * 20)

    #calculate number of 10 bills
    ten_bills = remaining_cost20 // 10

    #sovle for remaining cash for 10's
    remaining_cost10 = remaining_cost20 - (ten_bills * 10)

    #calculate number of 5 bills
    
    five_bills = remaining_cost10 // 5
    remaining_cost5 = remaining_cost10 - (five_bills * 5)

    #calculate number of 1 bills
    
    one_bills = remaining_cost5 // 1

    #solve for the remaining amount of cash
    remaining_costtotal = remaining_cost5 - (one_bills * 1)

    #print the values
    
    print('beep boo000Oop bot')
    print('you asked for $ ', cash_withdraw, 'that returns: ')
    print('$50 bills ', fifty_bills)
    print('$20 bills ', twenty_bills)
    print('$10 bills ', ten_bills)
    print('$5 bills ', five_bills)
    print('$1 bills ', one_bills)       

main()
    
    
    
    
    
    
    
                        
