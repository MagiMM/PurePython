class Calculator:
    """
    Klasa Calculator do wykonywania podstawowych operacji arytmetycznych.

    Attributes:
        op1 (float): Pierwszy operand
        op2 (float): Drugi operand
    """

    def __init__(self, op1: float, op2: float):
        """
        Inicjalizuje obiekt  Calculator z dwoma operandami.

        Args:
            op1 (float): Pierwszy operand
            op2 (float): Drugi operand
        """
        self.op1 = op1
        self.op2 = op2

    def sum(self) -> float:
        """
        Oblicza sumę dwóch operandów.

        Returns:
            float: Suma op1 i op2
        """
        return self.op1 + self.op2

    def subtract(self) -> float:
        """
        Oblicza różnicę dwóch operandów.

        Returns:
            float: Różnica op1 - op2
        """
        return self.op1 - self.op2

    def multiply(self) -> float:
        """
        Oblicza iloczyn dwóch operandów.

        Returns:
            float: Iloczyn op1 * op2
        """
        return self.op1 * self.op2

    def divide(self) -> float:
        """
        Oblicza iloraz dwóch operandów.

        Returns:
            float: Iloraz op1 / op2

        Raises:
            ZeroDivisionError: Gdy op2 wynosi 0
        """
        if self.op2 == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero!")
        return self.op1 / self.op2


# Przykład użycia:
if __name__ == "__main__":
    # Tworzenie obiektu kalkulatora
    calc = Calculator(10.0, 5.0)

    # Wykonywanie operacji
    print(f"Suma: {calc.sum()}")  # 15.0
    print(f"Różnica: {calc.subtract()}")  # 5.0
    print(f"Iloczyn: {calc.multiply()}")  # 50.0
    print(f"Iloraz: {calc.divide()}")  # 2.0

    # Przykład z innymi wartościami
    calc2 = Calculator(20, 4)
    print(f"\nNowy kalkulator (20, 4):")
    print(f"Suma: {calc2.sum()}")  # 24.0
    print(f"Różnica: {calc2.subtract()}")  # 16.0
    print(f"Iloczyn: {calc2.multiply()}")  # 80.0
    print(f"Iloraz: {calc2.divide()}")  # 5.0

    # Przykład obsługi błędu dzielenia przez zero
    calc3 = Calculator(10, 0)
    try:
        print(f"\nDzielenie przez zero: {calc3.divide()}")
    except ZeroDivisionError as e:
        print(f"Błąd: {e}")
