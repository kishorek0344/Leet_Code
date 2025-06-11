class Solution(object):
    def isAnagram(self, s, t):
        result_1 = list(map(lambda x : list(x), s))
        result_2 = list(map(lambda x : list(x), t))
        result_1.sort()
        result_2.sort()
        if result_1 == result_2:
            return True
        else:
            return False
            
        