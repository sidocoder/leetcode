class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"  
        for _ in range(2, n + 1):
            current = ""
            count = 1

            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    current += str(count) + result[i - 1]
                    count = 1

            current += str(count) + result[-1]
            result = current

        return result
