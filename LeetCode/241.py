# 241. Different Ways to Add Parentheses

### flow ###
# 1. divide: Make a list of each number and operator as elements.
# 2. conquer: Calculate small expression.
# 3. combine: Combine each result of each calculation.


class Solution:
    OPERATORS = '+-*'

    ## calculator
    def calculate(self, val1:int, val2:int, operator:str):
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        else:
            return val1 * val2


    ## divide and conquer 
    def divide_and_conquer(self, expression:list):
        # when expression has a number
        if len(expression) == 1:
            return [int(expression[0])]
        # when expression has an operator and two numbers
        elif len(expression) == 3:
            return [self.calculate(int(expression[0]), int(expression[2]), expression[1])]

        results = []
        for i in range(1, len(expression), 2):
            # divide 
            left_expression = expression[:i]
            right_expression = expression[i+1:]
            operator = expression[i]

            # conquer and combine
            left_results = self.divide_and_conquer(left_expression)
            right_results = self.divide_and_conquer(right_expression)

            for left in left_results:
                for right in right_results:
                    results.append(self.calculate(left, right, operator))
        return results
        
        
    def diffWaysToCompute(self, expression: str):
        expression_list = []
        expression_list.append(expression)
        
        ## make a list of each operator and number as elements.
        for k in self.OPERATORS:
            temp = []
            for i in expression_list:
                result = i.split(k)
                if len(result) > 1:
                    for j in range(1, len(result)*2-1, 2):
                        result.insert(j, k)
                temp.extend(result)
            expression_list = temp[:]
        return self.divide_and_conquer(expression_list)