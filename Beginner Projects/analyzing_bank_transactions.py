''' In this project we organize and analyze bank transactions'''

''' Here our code is in US cents'''
transactions_in_cents = [1000, -450, 7500, -3475, 13000, -8150, 25000, -850, 0, -1125, -600, 102550, -25025, 6500, -3850, -2500, 1875, 4000]
print ("Transactions (cents):")
print (transactions_in_cents)

''' Convert from cents to dollars'''
transactions = [dollar/100 for dollar in transactions_in_cents]
#(OPTIONAL TO VERIFY CODE WORKS) print(transactions)

transactions.sort()
print("Sorted Transactions:")
#(OPTIONAL TO VERIFY CODE WORKS) print(transactions)

'''Generate new filtered lists using list comprehension to include deposits(negative numbers) and withdrawals (positive numbers)'''
deposits = [dollar for dollar in transactions if dollar >= 0]
withdrawals = [dollar for dollar in transactions if dollar < 0]
print("Deposits:")
print(deposits)
print("Withdrawals:")
print(withdrawals)

'''create a function to convert negative numbers (withdrawals) into their positive equivalent'''
def invert_negative_num(negative_num):
  positive_num = negative_num * -1
  return positive_num

'''Put above into use by converting each amount in withdrawals into positive number all at once'''
withdrawals = [invert_negative_num(withdrawal) for withdrawal in withdrawals]
print("Withdrawals (positive values):")
print(withdrawals)

'''Here we use slice notation to create new list containing our 5 largest withdrawals'''
largest_withdrawals = withdrawals[:5]
print("Largest Withdrawals:")
print(largest_withdrawals)

'''Here we better understand our financial patterns, and convert floating points to integers '''
average_deposit = sum(deposits) / len(deposits)
average_deposit = int(average_deposit)
average_withdrawal = sum (withdrawals) / len(withdrawals)
average_withdrawal = int(average_withdrawal)
print("Average Deposit (int):")
print(average_deposit)
print("Average Withdrawal (int):")
print(average_withdrawal)

'''Lastly we get our current account balance'''
balance = sum(transactions)
print("Balance:")
print(balance)

"""During this project we converted transactions from cents to dollars,
   sorted them, created new lists of deposits, withdrawals, and largest withdrawals, 
   and calculated average transactions and final account balance."""

''' Additional Tasks we can do:
1. Calculate the total number of transactions
2. Create a new list to keeps track of the running balance after each transaction
3. Write a function to print all transactions between passed-in min and max values.'''