class Numbers:
    def Sum(n1, n2, n3):
        number = n1 + n2 + n3
        return number

    def Subtraction(n1, n2, n3):
        number = n1 - n2 - n3
        return number

    def Multiply(n1, n2, n3):
        number = n1 * n2 * n3
        return number

    def Division(n1, n2, n3):
        number = n1 / n2 / n3
        return number

number = Numbers.Sum(2, 2, 2)
print(number)