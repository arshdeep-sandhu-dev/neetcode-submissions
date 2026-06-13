class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d={"+","-","*","/"}
        stack = []
        for token in tokens:
            if token in d:
                
                firstNum = int(stack.pop())
                secondNum = int(stack.pop())
                print(str(secondNum)+" "+ str(firstNum))
                if (token == "+"):
                    token=firstNum+secondNum
                elif (token == "-"):
                    token=secondNum-firstNum
                elif (token == "/"):
                    token=secondNum/firstNum
                else:
                    token=firstNum*secondNum
                print(token)
            stack.append(int(token))
        return stack[-1]