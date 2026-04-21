class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for i in strs:
            r = r + i + '-' 
        return r
    def decode(self, s: str) -> List[str]:
        lis = s.split('-')

        return lis[:-1]
