#Determine whether an integer is a palindrome. Do this without extra space.

def isPalindrome(x):
    #Negative numbers can't be palindromes
    #Neither can multiples of 10 since you would need a 0
    #at the start. Only exception is 0 itself
    if (x < 0) or (x % 10 == 0 and x != 0):
        return False

    #Reverse half the number. You know you've reached halfway
    #when the orig num becomes smaller than revNum.
    #Since we only reverse half the number, no need to worry
    #about overflow
    revNum = 0
    while x > revNum:
        revNum = revNum*10 + (x % 10)
        x = int(x/10)

    #Case even digits: If both numbers are same, we're done
    #Case odd digits: The middle digit will be in LSB of revNum. Ignore
    return x == revNum or x == int(revNum/10)

if __name__ == "__main__":
    x = int(input())
    print (isPalindrome(x))
