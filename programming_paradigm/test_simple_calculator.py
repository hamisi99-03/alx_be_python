import unittest
from simple_calculator  import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(1,3),4)
        self.assertEqual(self.calc.add(-1,1),0)
        self.assertEqual(self.calc.add(-1,-1),-2)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4,3),1)
        self.assertEqual(self.calc.subtract(5,-1),6)
        self.assertEqual(self.calc.subtract(-1,-1),0)

    def test_division(self):
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertEqual(self.calc.divide(5,-1),-5)
        self.assertEqual(self.calc.divide(-1,-1),1)
        with self.assertRaises(ValueError):
          self.calc.divide(10,0)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4,3),12)
        self.assertEqual(self.calc.multiply(5,-1),-5)
        self.assertEqual(self.calc.multiply(-1,-1),1)
if __name__ == '__main__':
    unittest.main()

