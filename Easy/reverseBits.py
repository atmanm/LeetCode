#Reverse bits of a given 32 bits unsigned integer.
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n >= 2**32:
            return 0
        binary = str(bin(n)[2:].zfill(32))
        return (int(binary[::-1],2))

if __name__ == "__main__":
    n = int(input().strip())
    print(Solution().reverseBits(n))
