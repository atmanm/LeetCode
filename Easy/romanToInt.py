#Given a roman numeral, convert it to an integer.
#Input is guaranteed to be within the range from 1 to 3999.

def getIntVal(c):
    intDict = {}
    intDict['I'] = 1
    intDict['V'] = 5
    intDict['X'] = 10
    intDict['L'] = 50
    intDict['C'] = 100
    intDict['D'] = 500
    intDict['M'] = 1000

    try:
        return intDict[c]
    except IndexError:
        return 0

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    num = 0
    i = 0
    while i < len(s):
        c = s[i]
        try:
            nextChar = s[i+1]
        except IndexError:
            nextChar = 0
        intValC = getIntVal(c)
        intValNext = getIntVal(nextChar)
        # if next char val is greater, combine current and next char
        #eg: IV is 4 (5-1 or V-I)
        if intValC < intValNext:
            num = num + intValNext - intValC
            i = i + 1
        else:
            num = num + intValC
        i = i + 1

    return num

if __name__ == "__main__":
    romanNum = str(input().strip())
    print (romanToInt(romanNum))
