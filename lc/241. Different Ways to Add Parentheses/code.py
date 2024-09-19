class Solution:
    operations = {"+": lambda x,y: x + y,
                 "-": lambda x,y: x - y,
                 "*": lambda x,y: x * y,
                }
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(len(expression)):
            op = expression[i]
            if op in self.operations:
                num1 = self.diffWaysToCompute(expression[:i])
                num2 = self.diffWaysToCompute(expression[i+1:])

                for n1 in num1:
                    for n2 in num2:
                        res.append(self.operations[op](n1,n2))
        if res == []:
            res.append(int(expression))

        return res
