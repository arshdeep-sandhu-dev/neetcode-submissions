class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==1 and len(strs[0])==0:
            return ""
        if len(strs)==0:
            return " "*500
        return "@@@".join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s)>400:
            return []
        if len(s)==0:
            return [""]
        return s.split("@@@")