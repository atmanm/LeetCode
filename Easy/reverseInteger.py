#Given a 32-bit signed integer, reverse digits of an integer.
def reverse(x):
    #Given 32 but integer, so make sure number within range.
    #Python ints are 64 bit (Max size is 2**64 -1)
    if x > 2**31:
        x = 0

    #Save the sign. We'll put it back once we're done
    negative = False
    if x < 0:
        negative = True
        x = int(x * -1)

    revNum = 0
    while(x):
        #Get the LSB, stick it into the MSB of rev_num.
        #Keep doing it till we're done
        digit = x % 10
        revNum = revNum*10 + digit
        x = int(x/10)

    #Did the reverse cause overflow? That's bad
    if revNum > 2**31:
        revNum = 0
        negative = False

    #Stick the sign back in
    if negative:
        return (revNum * -1)
    else:
        return revNum

if __name__ == "__main__":
    x = int(input())
    print(reverse(x))
