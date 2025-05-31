class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start with the first string as the prefix candidate
        prefix = strs[0]
        
        for s in strs[1:]:
            # Shorten prefix until it matches the start of string s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove last char
                if prefix == "":
                    return ""
        return prefix
