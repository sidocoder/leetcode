class Solution:
    def validStrings(self, n: int) -> List[str]:
        valid_strings = []
    
    
        for bits in product("01", repeat=n):
            binary_str = "".join(bits)
            if "00" not in binary_str:  
                valid_strings.append(binary_str)
        
        return valid_strings
            