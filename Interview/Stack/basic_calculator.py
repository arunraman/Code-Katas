import operator

class Solution(object):
    def basicCalculator_2(self, s):
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in xrange(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = s[i]
                num = 0
        return sum(stack)

    def basicCalculator_1(self, s):
        s = ''.join(s.split() + ['+'])
        stack = [1]
        lo = 0
        ret = 0
        for hi, c in enumerate(s):
            if not c.isdigit():
                if hi > lo:
                    n = int(s[lo:hi])
                    ret += reduce(operator.mul, stack) * n
                if c == '+':
                    stack[-1] = 1
                elif c == '-':
                    stack[-1] = -1
                elif c == '(':
                    stack.append(1)
                elif c == ')':
                    stack.pop()
                lo = hi + 1
        return ret

    def calculate_2(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                        (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def calculate_1(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '+' or s[i] == '-':
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)




    # def compute(self, operands, operators):
    #     left, right = operands.pop(), operands.pop()
    #     op = operators.pop()
    #     if op == '+':
    #         operands.append(left + right)
    #     elif op == '-':
    #         operands.append(left - right)


S = Solution()
print S.basicCalculator_1("1 + 1") # = 2
print S.basicCalculator_1(" 2-1 + 2 ") # = 3
print S.calculate_1("(1+(4+5+2)-3)+(6+8)") # = 23)