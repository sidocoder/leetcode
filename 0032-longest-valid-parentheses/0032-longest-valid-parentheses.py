class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack = []
        # count = 0
        # for char in s:
        #     if stack and char == ')' and stack[-1] == "(":
        #             stack.pop() 
        #             count += 1
        #     else:
        #         count = 0
        #         stack.append(char)
        
        # return 2 * count

        stack = [-1]  
        count = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)  
                else:
                    count = max(count, i - stack[-1])

        return count