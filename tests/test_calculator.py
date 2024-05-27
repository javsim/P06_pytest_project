from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        a = 100
        b = 50
        cal = Calculator()


        result = cal.subtract(a, b)

        # assert
        expected = 50
        assert result == expected

    def test_multiply(self):
        a = 100 
        b = 50
        cal = Calculator()

        # act
        result = cal.multiply(a, b)
        # assert
        expected = 5000
        assert result == expected

    def test_divide(self):
        a = 100
        b = 0
        cal = Calculator()

        result = cal.divide(a, b)

        expected = 2
        assert result == expected
