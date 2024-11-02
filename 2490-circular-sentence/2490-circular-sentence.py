class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # Split the sentence into a list of words
        words = sentence.split()
        
        # Check each consecutive pair of words
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        
        # Check the circular condition: last word to first word
        if words[-1][-1] != words[0][0]:
            return False
        
        # If all conditions are satisfied, return True
        return True
