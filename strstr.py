class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle):
            return None
        i = 0
        while i < len(haystack)-len(needle)+1:
            j = 0
            k = i
            while j < len(needle):
                if haystack[k] == needle[j]:
                    j += 1
                    k += 1
                else:
                    break
            if j == len(needle):
                break
            else:
                i += 1
        if i == len(haystack)-len(needle)+1:
            return None
        else:
            return haystack[i:]