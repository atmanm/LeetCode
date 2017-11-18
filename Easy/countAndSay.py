#Given an integer n, generate the nth term of the count-and-say sequence.
#Eg: n = 1 ==> 1
#    n = 2 ==> 11 (Reading previous as One 1)
#    n = 3 ==> 21 (Reading previous as Two 1)
#    n = 4 ==> 1211 (Reading previous as One 2 One 1)
#    n = 5 ==> 111221 (Reading previous as One 1 One 2 Two 1)


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 0:
            return '0'
        #Base case
        string = '1'

        #We want to cover cases for n = 1 through n
        for _ in range(1,n):
            #Overwrite s with the string corresponding to n = i
            #For that, start with first char in s, count. Continue till end then
            #overwrite
            [temp, idx, count] = ['', 0, 1]
            while idx < len(string):
                try:
                    same = (string[idx] == string[idx + 1])
                except IndexError:
                    same = False
                if same:
                    [count, idx] = [count+1, idx+1]
                    continue
                else:
                    [temp,count] = [temp+str(count)+string[idx], 1]
                idx += 1

            string = temp

        return string


if __name__ == "__main__":
    try:
        n = int(input())
    except ValueError:
        n = 0
    print(Solution().countAndSay(n))
