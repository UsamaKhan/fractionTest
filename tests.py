from fraction import Fraction
import unittest


class TestInit(unittest.TestCase):
    # several of these will need to check to see if an exception is raised
    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError, msg="Denominator of zero fails to raise DivByZero"):
            Fraction(1, 0)

    def test_default(self):
        a = Fraction()
        self.assertTrue(a.numerator == 0 & a.denominator == 1,
                        "Fails to initialize correctly with default arguments")

    def test_one_arg(self):
        arg1 = 1
        a = Fraction(arg1)
        self.assertTrue(a.numerator == arg1 & a.denominator == 1,
                        "Fails to initialize correctly with one argument")

    def test_two_arg(self):
        arg1 = 1
        arg2 = 2
        a = Fraction(arg1, arg2)
        self.assertTrue(a.numerator == arg1 & a.denominator == arg2,
                        "Fails to initialize correctly with two arguments")

    # noinspection PyArgumentList
    def test_three_arg(self):
        with self.assertRaises(TypeError, msg="Three args provided"):
            Fraction(1, 2, 3)

    def test_invalid_arg(self):
        with self.assertRaises(TypeError, msg="Invalid argument"):
            Fraction("hello")

    def test_neg_denominator(self):
        arg1 = 1
        arg2 = -2
        a = Fraction(arg1, arg2)
        self.assertTrue(a.numerator == -arg1 & a.denominator == -arg2,
                        "Fails to move sign from denominator to numerator")

    def test_reduced(self):
        arg1 = 10
        arg2 = 20
        a = Fraction(arg1, arg2)
        self.assertTrue(a.numerator == 1 & a.denominator == 2,
                        "Fails to reduce fraction")


class TestStr(unittest.TestCase):
    def test_display_fraction(self):
        a = Fraction(1, 2)
        self.assertEqual("1/2", a.__str__(),
                         "Fails to display fraction as string")

    def test_display_int(self):
        a = Fraction(2, 1)
        self.assertEqual("2", a.__str__(),
                         "Fails to display int when denominator is 1")

    def test_display_neg(self):
        a = Fraction(-1, 2)
        self.assertEqual("-1/2", a.__str__(),
                         "Fails to display negative fraction")


class TestFloat(unittest.TestCase):
    def test_float(self):
        a = Fraction(3, 4)
        self.assertEqual(0.75, a.__float__(),
                         "Fails to convert to float")

    def test_float_int(self):
        a = Fraction(1, 1)
        self.assertEqual(1.0, a.__float__(),
                         "Fails to convert to float when denominator is 1")

    def test_float_neg(self):
        a = Fraction(-1, 2)
        self.assertEqual(-0.5, a.__float__(),
                         "Fails to convert negative fraction to float")

    def test_float_zero(self):
        a = Fraction(0, 1)
        self.assertEqual(0.0, a.__float__(),
                         "Fails to convert zero to float")


class TestEq(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Fraction(1, 2)
        self.b = Fraction(1, 2)
        self.c = Fraction(2, 4)
        self.d = Fraction(1, 3)
        self.e = Fraction(-1, 2)

    def test_equal(self):
        self.assertTrue(self.a == self.b,
                        "Fails to compare equal fractions")

    def test_equal_reduced(self):
        self.assertTrue(self.a == self.c,
                        "Fails to compare equal fractions when reduced")

    def test_not_equal(self):
        self.assertFalse(self.a == self.d,
                         "Fails to compare unequal fractions")

    def test_not_equal_neg(self):
        self.assertFalse(self.a == self.e,
                         "Fails to compare unequal fractions")

    def test_not_equal_type(self):
        self.assertFalse(self.a == 1,
                         "Fails to compare unequal types")


class TestAdd(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Fraction(1, 2)
        self.b = Fraction(1, 3)
        self.c = Fraction(2, 4)
        self.d = Fraction(-1, 2)

    def test_add(self):
        self.assertEqual(Fraction(5, 6), self.a + self.b,
                         "Fails to add fractions")

    def test_add_self(self):
        self.assertEqual(Fraction(1, 1), self.a + self.a,
                         "Fails to add fraction to itself")

    def test_add_reduced(self):
        self.assertEqual(Fraction(1, 1), self.a + self.c,
                         "Fails to add fractions when reduced")

    def test_add_neg(self):
        self.assertEqual(Fraction(0, 1), self.a + self.d,
                         "Fails to add negative fractions")

    def test_add_int(self):
        self.assertEqual(Fraction(5, 2), self.a + 2,
                         "Fails to add int to fraction")

    def test_add_float(self):
        self.assertEqual(Fraction(1, 1), self.a + 0.5,
                         "Fails to add float to fraction")

    def test_add_type(self):
        with self.assertRaises(TypeError, msg="Fails to add invalid type"):
            self.a + "hello"


class TestSub(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Fraction(1, 2)
        self.b = Fraction(1, 3)
        self.c = Fraction(2, 4)
        self.d = Fraction(-1, 2)

    def test_sub(self):
        self.assertEqual(Fraction(1, 6), self.a - self.b,
                         "Fails to subtract fractions")

    def test_sub_self(self):
        self.assertEqual(Fraction(0, 1), self.a - self.a,
                         "Fails to subtract fraction from itself")

    def test_sub_reduced(self):
        self.assertEqual(Fraction(0, 1), self.a - self.c,
                         "Fails to subtract fractions when reduced")

    def test_sub_neg(self):
        self.assertEqual(Fraction(1, 1), self.a - self.d,
                         "Fails to subtract negative fractions")

    def test_sub_int(self):
        self.assertEqual(Fraction(-3, 2), self.a - 2,
                         "Fails to subtract int from fraction")

    def test_sub_float(self):
        self.assertEqual(Fraction(0, 1), self.a - 0.5,
                         "Fails to subtract float from fraction")

    def test_sub_type(self):
        with self.assertRaises(TypeError, msg="Fails to subtract invalid type"):
            self.a - "hello"


class TestMul(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Fraction(1, 2)
        self.b = Fraction(1, 3)
        self.c = Fraction(2, 4)
        self.d = Fraction(-1, 2)

    def test_mul(self):
        self.assertEqual(Fraction(1, 6), self.a * self.b,
                         "Fails to multiply fractions")

    def test_mul_self(self):
        self.assertEqual(Fraction(1, 4), self.a * self.a,
                         "Fails to multiply fraction by itself")

    def test_mul_reduced(self):
        self.assertEqual(Fraction(1, 4), self.a * self.c,
                         "Fails to multiply fractions when reduced")

    def test_mul_neg(self):
        self.assertEqual(Fraction(-1, 4), self.a * self.d,
                         "Fails to multiply negative fractions")

    def test_mul_int(self):
        self.assertEqual(Fraction(1, 1), self.a * 2,
                         "Fails to multiply int by fraction")

    def test_mul_float(self):
        self.assertEqual(Fraction(1, 4), self.a * 0.5,
                         "Fails to multiply float by fraction")

    def test_mul_type(self):
        with self.assertRaises(TypeError, msg="Fails to multiply invalid type"):
            self.a * "hello"


class TestTruediv(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Fraction(1, 2)
        self.b = Fraction(1, 3)
        self.c = Fraction(2, 4)
        self.d = Fraction(-1, 2)

    def test_truediv(self):
        self.assertEqual(Fraction(3, 2), self.a / self.b,
                         "Fails to divide fractions")

    def test_truediv_self(self):
        self.assertEqual(Fraction(1, 1), self.a / self.a,
                         "Fails to divide fraction by itself")

    def test_truediv_reduced(self):
        self.assertEqual(Fraction(1, 1), self.a / self.c,
                         "Fails to divide fractions when reduced")

    def test_truediv_neg(self):
        self.assertEqual(Fraction(-2, 1), self.a / self.d,
                         "Fails to divide negative fractions")

    def test_truediv_int(self):
        self.assertEqual(Fraction(1, 4), self.a / 2,
                         "Fails to divide int by fraction")

    def test_truediv_float(self):
        self.assertEqual(Fraction(1, 1), self.a / 0.5,
                         "Fails to divide float by fraction")

    def test_truediv_type(self):
        with self.assertRaises(TypeError, msg="Fails to divide invalid type"):
            self.a / "hello"
