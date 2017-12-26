class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        str1 = format(x, '#032b')
        str2 = format(y, '#032b')

        print(str2)
        print(str1)

        counter = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                counter += 1

        return counter

if __name__ == '__main__':

    s = Solution()
