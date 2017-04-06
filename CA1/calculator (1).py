# 10353830 Derek Baker
import math

# Create GUI
class Menu(object):
	def start(self):
		print"""
		\t*****************************************************
		\t*****************************************************
		\t################## CALCULATOR #######################
		\t*****************************************************
		\t************ The functions availabe are: ************
		\t****                                             ****
		\t****   [ + = Addition ]      [ c = cos ]         ****
		\t****   [ / = Division ]      [ t = tan ]         ****
		\t****   [ * = Multiply ]      [ s = sin ]         ****
		\t****   [ - = Subtraction ]   [ p = Power ]       ****
		\t****   [ r = Square root ]   [ e = Exponential]  ****
		\t****                                             ****
		\t**************** Press 'Q' to Quit ******************
		\t*****************************************************
		\t*****************************************************\n\n"""
	
	def quit(self):
		print """
		\t*****************************************************
		\t#################### BYE! ###########################
		\t*****************************************************\n\n"""
# Create functions	
class Calculator(object):
	def add(self,num1,num2):
		plus = num1 + num2
		return plus
	def sub(self,num1,num2):
		sub = num1 - num2
		return sub
	def multi(self,num1,num2):
		by = num1 * num2
		return  by
	def div(self,num1,num2):
		if num2 == 0:
			return "Can't divide by 0"
		else:
			over = num1 / num2
			return over
	def power(self,num1,num2): 
		return pow(num1,num2)
	def sqrt(self,num1):
		return math.sqrt(num1)
	def exp(self, num1):
		exp = num1**2
		return exp
	def sin(self, num1):
		return math.sin(math.radians(num1))
	def cos(self, num1):
		return round(math.cos(math.radians(num1)),5)
	def tan(self,num1):
		return math.tan(math.radians(num1))

# create App
while True:
	menu = Menu() # Initilise menu
	menu.start() # show welcome screen
	sum = Calculator() # initilise functions
# Get imput
	num1 = raw_input('Please enter No 1\n') 
	if num1=='q':
		menu.quit()
		break
	func = raw_input('Please enter function /, *, +, -, c, r, e, s, c t or p\n')
	func = func.lower()
	if func=='q':
		menu.quit()
		break
	if func in ['+','-','*','/','p']:
		num2 = raw_input('Please enter No 2\n')
		if num2=='q':
			menu.quit()
			break
		if num1 == '0' and func == '/' or num2 == '0' and func == '/':
			print 'You cannot divide by zero'
			continue
# idenify operation with failsafe
	try:
		num1 = float(num1)
		if func in ['+','-','*','/','p']:
			num2 = float(num2)
		if func == '/':
			result = sum.div(num1,num2)
		elif func == '*':
			result = sum.multi(num1,num2)
		elif func == '-':
			result = sum.sub(num1,num2)
		elif func == '+':
			result = sum.add(num1,num2)
		elif func == 'p':
			result = sum.power(num1,num2)
		elif func == 'r':
			result = sum.sqrt(num1)
		elif func == 'e':
			result = sum.exp(num1)
		elif func == 's':
			result = sum.sin(num1)
		elif func == 'c':
			result = sum.cos(num1)
		elif func == 't':
			result = sum.tan(num1)
		else:
			print 'Invalid function'
			continue
	except:
		print 'Please use numbers'
		continue
# Output
	print "The answer is {}\n".format(result)
# Check to loop
	if 'y' == raw_input('Do you wish to convert again? y / n '):
		continue
	else:
		menu.quit()
		break