class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = True
        sJuice = re.sub(r'[^a-zA-Z0-9]', '', s)
        sKANK = sJuice.lower()
        i = 0
        j = len(sKANK)-1
        while i <= j:
            
            if sKANK[i] !=sKANK[j]:
                print(sKANK[i], sKANK[j])
                return False
            i+=1
            j-=1
        return res
                
        