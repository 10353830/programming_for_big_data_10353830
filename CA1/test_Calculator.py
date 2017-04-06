# 10353830 Derek Baker
import unittest
# get calculator App
from calculator import *


# test the calculator functionality
class TestCalculator(unittest.TestCase):

	def setUp(self):
		self.calc = Calculator()
		
# Test the all functionalities

	def test_calculator_addition_validation(self):
		result = self.calc.add(20, 13)
		self.assertEqual(33, result)
		result = self.calc.add(3,5)
		self.assertEqual(8, result)
		result = self.calc.add(4, -6)
		self.assertEqual(-2, result)

	def test_calculator_subtraction_validation(self):
		result = self.calc.sub(3, 2)
		self.assertEqual(1, result)
		result = self.calc.sub(25, 7)
		self.assertEqual(18, result)
		result = self.calc.sub(6, -4)
		self.assertEqual(10, result)
		
	def test_calculator_multiply_validation(self):
		result = self.calc.multi(3, 6)
		self.assertEqual(18, result)
		result = self.calc.multi(-3, 6)
		self.assertEqual(-18, result)
		
	def test_calculator_divide_validation(self):
		result = self.calc.div(8, 2)
		self.assertEqual(4, result)
		result = self.calc.div(-8, 2)
		self.assertEqual(-4, result)
		
	def test_calculator_power_validation(self):
		result = self.calc.power(3, 3)
		self.assertEqual(27, result)
		result = self.calc.power(-3, 3)
		self.assertEqual(-27, result)

	def test_calculator_square_root_validation(self):
		result = self.calc.sqrt(16)
		self.assertEqual(4, result)
		result = self.calc.sqrt(49)
		self.assertEqual(7, result)

	def test_calculator_Exponential_validation(self):
		result = self.calc.exp(7)
		self.assertEqual(49, result)
		result = self.calc.exp(-7)
		self.assertEqual(49, result)
		
	def test_calculator_sin_validation(self):
		result = self.calc.sin(30)
		self.assertEqual(.5, round(result,5))
		result = self.calc.sin(90)
		self.assertEqual(1, round(result,5))

	def test_calculator_cos_validation(self):
		result = self.calc.cos(90)
		self.assertEqual(0, round(result,5))
		result = self.calc.cos(.01)
		self.assertEqual(1, round(result,5))

	def test_calculator_tan_validation(self):
		result = self.calc.tan(30)
		self.assertEqual(.57735, round(result,5))		
		result = self.calc.tan(45)
		self.assertEqual(1, round(result,5))
	

if __name__ == '__main__':
    unittest.main()
