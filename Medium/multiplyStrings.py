#Given two non-negative integers num1 and num2 represented as strings, return
#the product of num1 and num2.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        len1 = len(num1)
        len2 = len(num2)

        result = [0]*(len1 + len2)

        for i, digit1 in enumerate(reversed(num1)):
            for j, digit2 in enumerate(reversed(num2)):
                int1 = ord(digit1) - ord('0')
                int2 = ord(digit2) - ord('0')

                resInt = int1 * int2

                resUnits = resInt%10
                resTens = resInt//10

                posUnits = len1+len2-1-(i+j)
                posTens = len1+len2-1-(i+j+1)

                result[posUnits] += resUnits
                result[posTens] += resTens

                if result[posUnits] > 9:
                    result[posUnits] %= 10
                    result[posUnits-1] += 1
                if result[posTens] > 9:
                    result[posTens] %= 10
                    result[posTens-1] += 1

        i  = 0
        while result[i] == 0 and len(result) > 1:
            result.pop(i)
        return ''.join(map(str, result[:]))

if __name__ == "__main__":
    num1 = str(input().strip())
    num2 = str(input().strip())

    print(Solution().multiply(num1, num2))
