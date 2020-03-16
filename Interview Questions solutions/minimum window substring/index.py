class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)

        if(len1 < len2):
            return ""

        hashPat = {}
        hashStr = {}

        for i in range(0, len2):
            if(hashPat.get(t[i]) is None):
                hashPat[t[i]] = 0
            hashPat[t[i]] += 1

        count = 0
        left = 0
        startIndex = -1
        minLen = float("inf")

        for right in range(0, len1):

            if(hashStr.get(s[right]) is None):
                hashStr[s[right]] = 0
            hashStr[s[right]] += 1
            if(hashPat.get(s[right]) is None):
                hashPat[s[right]] = 0
            if (

                hashPat.get(s[right]) != 0 and
                hashStr.get(s[right]) <= hashPat.get(s[right])
            ):
                count += 1  # keep incrementing the count if string hash is less then pattern hash
            # count==len2 means a window is found that contains all character of pattern string
            if (count == len2):

                if(hashStr.get(s[left]) is None):
                    hashStr[s[right]] = 0
                if(hashPat.get(s[left]) is None):
                    hashPat[s[right]] = 0
                while (
                    hashStr.get(s[left]) > hashPat.get(s[left]) or
                    hashPat.get(s[left]) == 0
                ):
                    #minimizing the windows range from left side

                    if (hashStr.get(s[left]) > hashPat.get(s[left])):
                        hashStr[s[left]] -= 1
                    left += 1  # incrementing the left pointer

                windowLen = right - left + 1  # calculating the windows length
                if (minLen > windowLen):
                    minLen = windowLen
                    startIndex = left

        if (startIndex == -1):
            return ""
        return s[startIndex:startIndex+minLen]
