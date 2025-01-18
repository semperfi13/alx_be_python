def add_number(*numbers: float) -> float:
    return sum(numbers)


class Calculator:
    def __init__(self, version: int):
        self.version = version

    def description(self):
        print(f"Currently running Calculator on version:{self.version}")

    @staticmethod
    def add_number(*numbers: float) -> float:
        return sum(numbers)

    @classmethod
    def add_calculator_name(cls, version: int, name: str):
        name: str = name
        return cls(version)


if __name__ == "__main__":
    # calc = Calculator(12)
    calc = Calculator.add_calculator_name(78, "Semperficalculator")
    print(calc.description())
