class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        for i in range(n+1):
            binary=bin(i)[2:]
            count=0
            for bit in binary:
                if bit=='1':
                    count=count+1
            output.append(count)
        return output
