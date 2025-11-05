# test_calculator.py
import pytest
from calculator import Calculator


class TestCalculator:
    """
    Kompleksowy zestaw testów dla klasy Calculator.
    """

    # --- Testy inicjalizacji ---

    def test_calculator_initialization_integers(self):
        """Test inicjalizacji z liczbami całkowitymi."""
        calc = Calculator(10, 5)
        assert calc.op1 == 10
        assert calc.op2 == 5

    def test_calculator_initialization_floats(self):
        """Test inicjalizacji z liczbami zmiennoprzecinkowymi."""
        calc = Calculator(10.5, 3.2)
        assert calc.op1 == 10.5
        assert calc.op2 == 3.2

    def test_calculator_initialization_negative_numbers(self):
        """Test inicjalizacji z liczbami ujemnymi."""
        calc = Calculator(-15, -5)
        assert calc.op1 == -15
        assert calc.op2 == -5

    def test_calculator_initialization_zero(self):
        """Test inicjalizacji z zerami."""
        calc = Calculator(0, 0)
        assert calc.op1 == 0
        assert calc.op2 == 0

    # --- Testy metody sum() ---

    def test_sum_positive_numbers(self):
        """Test dodawania liczb dodatnich."""
        calc = Calculator(10, 5)
        assert calc.sum() == 15

    def test_sum_negative_numbers(self):
        """Test dodawania liczb ujemnych."""
        calc = Calculator(-10, -5)
        assert calc.sum() == -15

    def test_sum_mixed_signs(self):
        """Test dodawania liczb o różnych znakach."""
        calc = Calculator(10, -5)
        assert calc.sum() == 5

    def test_sum_with_zero(self):
        """Test dodawania z zerem."""
        calc = Calculator(10, 0)
        assert calc.sum() == 10

    def test_sum_floats(self):
        """Test dodawania liczb zmiennoprzecinkowych."""
        calc = Calculator(10.5, 3.2)
        assert calc.sum() == pytest.approx(13.7)

    # --- Testy metody subtract() ---

    def test_subtract_positive_numbers(self):
        """Test odejmowania liczb dodatnich."""
        calc = Calculator(10, 5)
        assert calc.subtract() == 5

    def test_subtract_negative_numbers(self):
        """Test odejmowania liczb ujemnych."""
        calc = Calculator(-10, -5)
        assert calc.subtract() == -5

    def test_subtract_result_negative(self):
        """Test odejmowania dającego wynik ujemny."""
        calc = Calculator(5, 10)
        assert calc.subtract() == -5

    def test_subtract_with_zero(self):
        """Test odejmowania z zerem."""
        calc = Calculator(10, 0)
        assert calc.subtract() == 10

    def test_subtract_floats(self):
        """Test odejmowania liczb zmiennoprzecinkowych."""
        calc = Calculator(10.5, 3.2)
        assert calc.subtract() == pytest.approx(7.3)

    # --- Testy metody multiply() ---

    def test_multiply_positive_numbers(self):
        """Test mnożenia liczb dodatnich."""
        calc = Calculator(10, 5)
        assert calc.multiply() == 50

    def test_multiply_negative_numbers(self):
        """Test mnożenia liczb ujemnych."""
        calc = Calculator(-10, -5)
        assert calc.multiply() == 50

    def test_multiply_mixed_signs(self):
        """Test mnożenia liczb o różnych znakach."""
        calc = Calculator(10, -5)
        assert calc.multiply() == -50

    def test_multiply_by_zero(self):
        """Test mnożenia przez zero."""
        calc = Calculator(10, 0)
        assert calc.multiply() == 0

    def test_multiply_floats(self):
        """Test mnożenia liczb zmiennoprzecinkowych."""
        calc = Calculator(2.5, 4.0)
        assert calc.multiply() == pytest.approx(10.0)

    # --- Testy metody divide() ---

    def test_divide_positive_numbers(self):
        """Test dzielenia liczb dodatnich."""
        calc = Calculator(10, 5)
        assert calc.divide() == 2.0

    def test_divide_negative_numbers(self):
        """Test dzielenia liczb ujemnych."""
        calc = Calculator(-10, -5)
        assert calc.divide() == 2.0

    def test_divide_mixed_signs(self):
        """Test dzielenia liczb o różnych znakach."""
        calc = Calculator(10, -5)
        assert calc.divide() == -2.0

    def test_divide_result_float(self):
        """Test dzielenia dającego wynik niecałkowity."""
        calc = Calculator(10, 3)
        assert calc.divide() == pytest.approx(3.3333333333)

    def test_divide_by_zero_raises_exception(self):
        """Test czy dzielenie przez zero podnosi wyjątek."""
        calc = Calculator(10, 0)
        with pytest.raises(ZeroDivisionError):
            calc.divide()

    def test_divide_by_zero_exception_message(self):
        """Test komunikatu wyjątku przy dzieleniu przez zero."""
        calc = Calculator(10, 0)
        with pytest.raises(ZeroDivisionError, match="Nie można dzielić przez zero!"):
            calc.divide()

    def test_divide_zero_by_number(self):
        """Test dzielenia zera przez liczbę."""
        calc = Calculator(0, 5)
        assert calc.divide() == 0.0

    def test_divide_floats(self):
        """Test dzielenia liczb zmiennoprzecinkowych."""
        calc = Calculator(7.5, 2.5)
        assert calc.divide() == pytest.approx(3.0)


# --- Testy parametryzowane ---

class TestCalculatorParametrized:
    """
    Testy parametryzowane dla różnych scenariuszy.
    """

    @pytest.mark.parametrize("op1, op2, expected", [
        (10, 5, 15),
        (0, 0, 0),
        (-5, -3, -8),
        (100, 200, 300),
        (1.5, 2.5, 4.0),
    ])
    def test_sum_parametrized(self, op1, op2, expected):
        """Test parametryzowany dodawania."""
        calc = Calculator(op1, op2)
        assert calc.sum() == pytest.approx(expected)

    @pytest.mark.parametrize("op1, op2, expected", [
        (10, 5, 5),
        (0, 0, 0),
        (5, 10, -5),
        (100, 50, 50),
        (7.5, 2.5, 5.0),
    ])
    def test_subtract_parametrized(self, op1, op2, expected):
        """Test parametryzowany odejmowania."""
        calc = Calculator(op1, op2)
        assert calc.subtract() == pytest.approx(expected)

    @pytest.mark.parametrize("op1, op2, expected", [
        (10, 5, 50),
        (0, 10, 0),
        (-5, -3, 15),
        (2, 3, 6),
        (2.5, 4, 10.0),
    ])
    def test_multiply_parametrized(self, op1, op2, expected):
        """Test parametryzowany mnożenia."""
        calc = Calculator(op1, op2)
        assert calc.multiply() == pytest.approx(expected)

    @pytest.mark.parametrize("op1, op2, expected", [
        (10, 5, 2.0),
        (20, 4, 5.0),
        (7, 2, 3.5),
        (100, 25, 4.0),
        (9, 3, 3.0),
    ])
    def test_divide_parametrized(self, op1, op2, expected):
        """Test parametryzowany dzielenia."""
        calc = Calculator(op1, op2)
        assert calc.divide() == pytest.approx(expected)


# --- Testy z fixtures ---

@pytest.fixture
def calc_10_5():
    """Fixture zwracający kalkulator z wartościami 10 i 5."""
    return Calculator(10, 5)


@pytest.fixture
def calc_zero():
    """Fixture zwracający kalkulator z zerowymi wartościami."""
    return Calculator(0, 0)


@pytest.fixture
def calc_negative():
    """Fixture zwracający kalkulator z wartościami ujemnymi."""
    return Calculator(-10, -5)


class TestCalculatorWithFixtures:
    """
    Testy wykorzystujące fixtures.
    """

    def test_all_operations_with_fixture(self, calc_10_5):
        """Test wszystkich operacji na jednym obiekcie z fixture."""
        assert calc_10_5.sum() == 15
        assert calc_10_5.subtract() == 5
        assert calc_10_5.multiply() == 50
        assert calc_10_5.divide() == 2.0

    def test_zero_operations(self, calc_zero):
        """Test operacji na zerach."""
        assert calc_zero.sum() == 0
        assert calc_zero.subtract() == 0
        assert calc_zero.multiply() == 0

    def test_negative_operations(self, calc_negative):
        """Test operacji na liczbach ujemnych."""
        assert calc_negative.sum() == -15
        assert calc_negative.subtract() == -5
        assert calc_negative.multiply() == 50
        assert calc_negative.divide() == 2.0


# --- Testy właściwości typu ---

class TestCalculatorTypes:
    """
    Testy sprawdzające typy zwracanych wartości.
    """

    def test_sum_returns_float(self):
        """Test czy sum() zwraca float."""
        calc = Calculator(10, 5)
        result = calc.sum()
        assert isinstance(result, (int, float))

    def test_subtract_returns_float(self):
        """Test czy subtract() zwraca float."""
        calc = Calculator(10, 5)
        result = calc.subtract()
        assert isinstance(result, (int, float))

    def test_multiply_returns_float(self):
        """Test czy multiply() zwraca float."""
        calc = Calculator(10, 5)
        result = calc.multiply()
        assert isinstance(result, (int, float))

    def test_divide_returns_float(self):
        """Test czy divide() zwraca float."""
        calc = Calculator(10, 5)
        result = calc.divide()
        assert isinstance(result, float)


# --- Testy brzegowe ---

class TestCalculatorEdgeCases:
    """
    Testy przypadków brzegowych.
    """

    def test_very_large_numbers(self):
        """Test z bardzo dużymi liczbami."""
        calc = Calculator(1e308, 1e308)
        assert calc.sum() == pytest.approx(2e308)

    def test_very_small_numbers(self):
        """Test z bardzo małymi liczbami."""
        calc = Calculator(1e-10, 1e-10)
        assert calc.sum() == pytest.approx(2e-10)

    def test_precision_with_floats(self):
        """Test precyzji z liczbami zmiennoprzecinkowymi."""
        calc = Calculator(0.1, 0.2)
        # Używamy pytest.approx() dla porównań float
        assert calc.sum() == pytest.approx(0.3)

    def test_negative_zero(self):
        """Test z ujemnym zerem."""
        calc = Calculator(-0.0, 5)
        assert calc.sum() == 5.0


if __name__ == "__main__":
    # Uruchomienie testów z terminala:
    # pytest test_calculator.py -v
    pytest.main([__file__, "-v"])
