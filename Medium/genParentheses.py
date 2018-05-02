#Given n pairs of parentheses, write a function to generate all combinations of
#well-formed parentheses.

class Solution(object):
    def generateParenthesis(self, n, openParen=0):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [')'*openParen]
        if openParen == 0:
            return ['('+x for x in self.generateParenthesis(n-1,1)]
        else:
            return ['('+x for x in self.generateParenthesis(n-1,openParen+1)]+\
                   [')'+x for x in self.generateParenthesis(n, openParen-1)]

if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().generateParenthesis(n))
