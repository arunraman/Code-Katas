class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i - 1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == '*' or s[i] == '/':
                # if (operators[-1] == '-'):
                #     operands[-1] = operands[-1] * -1
                #     operators.pop()
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and ((operators[-1] == '*' or operators[-1] == '/')):
                    self.compute(operands, operators)
                operators.append(s[i])

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        #if len(operands) != len(operators):
        #    left_operator, right_operator = operators.pop(), operators[-1].pop()
        #print left_operator, right_operator
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(float(left) / float(right))

S = Solution()
# #print S.calculate('1 * 1')
# print S.calculate('1 * -1')
# #print S.calculate('1 + 4 - 2')
# #print S.calculate('1 * 10 - 7 / 4')