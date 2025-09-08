'''You are working as a Manager in a bank. At the end of the day, You have to send a report to your supervisors which consists of count of distinct accounts that were operated upon on that particular day.
You are given a list containing the account numbers of the customers of the bank according to their time of arrival in the bank.
You have to tell the count of distinct accounts.'''
def main():
    N = int(input()) 
    accounts = list(map(int, input().split()))  
    distinct_accounts = set(accounts)# Use set to remove duplicates  
    print(len(distinct_accounts))  
 # Write code here 

main()