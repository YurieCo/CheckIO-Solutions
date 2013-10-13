#Your optional code here
#You can import some modules or create additional functions


def checkio(balance, withdrawal):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.  
    for i in withdrawal:
            if i%5==0 and balance>i>0:
                balance-=i
                balance-=1
    return balance
            
   

#Some hints:
#Make sure you loop through the withdrawal amounts
#make sure you have enough money to withdraw,
#otherwise don't (return the same balance)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(120, [10, 20, 30]) == 57, 'First example'

    # With one Insufficient Funds, and then withdraw 10 $
    assert checkio(120, [200, 10]) == 109, 'Second example'

    #with one incorrect amount
    assert checkio(120, [3, 10]) == 109, 'Third example'

    assert checkio(120, [200, 119]) == 120, 'Fourth example'

    assert checkio(120, [120, 10, 122, 2, 10, 10, 30, 1]) == 56, "It's mixed all base tests"

    assert checkio(120, [-10]) == 120, 'Negative value'
    
    