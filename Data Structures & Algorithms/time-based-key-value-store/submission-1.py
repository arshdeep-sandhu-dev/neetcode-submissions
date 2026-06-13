class TimeMap:

    def __init__(self):
        self.keyValue={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyValue:
            self.keyValue[key] = []
        self.keyValue[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.keyValue:
            return ""
        l,r = 0,len(self.keyValue[key])-1
        values = self.keyValue[key]
        res=""
        while (l<=r):
            m = (l + r) // 2
            if (values[m][1] <= timestamp):
                l = m + 1   
                res= values[m][0]
            else:
                r = m - 1
        return res
