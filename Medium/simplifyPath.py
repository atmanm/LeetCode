#Given an absolute path for a file (Unix-style), simplify it.

import re
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        directories = [d for d in path.split("/") if d != "." and d != ""]

        finalPath = []

        for directory in directories:
            if directory == "..":
                try:
                    finalPath.pop()
                except IndexError:
                    pass
            else:
                finalPath.append(directory)

        return "/" + "/".join(finalPath)

if __name__ == "__main__":
    path = str(input().strip())
    print(Solution().simplifyPath(path))
