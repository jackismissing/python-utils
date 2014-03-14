'''
Converts a positive integer into a binary number
Floats are parse as integers
Usage : num = ToBin(your_number)
'''
class ToBin():
	def __init__(self, num):
		self.convert(num)
	
	def convert(self, num):
		result = ""
		try:
			num = int(num)
			if num < 0:
				try_again = raw_input('Please enter a valid positive integer: ')		
				self.convert(try_again)
			elif num == 0:
				result = "0"
			else:
				while num > 0:
					result = str(num%2) + result
					num = num/2
		except ValueError:	
			try_again = raw_input('Please enter a valid positive integer: ')
			self.convert(try_again)				
		print result
	

