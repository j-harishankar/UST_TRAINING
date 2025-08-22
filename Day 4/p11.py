class AddSub:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


class MulDiv:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b if self.b != 0 else "Division by zero"


def main():
    a, b = 4, 1
    addsu = AddSub(a, b)
    mudi = MulDiv(a, b)

    print(addsu.add())  # 5
    print(addsu.sub())  # 3
    print(mudi.mul())   # 4
    print(mudi.div())   # 4.0


if __name__ == '__main__':
    main()
