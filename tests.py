import unittest-
from Learnme import summation

class SummationTest(unittest.TestCase):
	
	def setUp(self):
		self.stuff = ['hi','mom']

	def test_checkzero(self):
		self.assertEqual(summation(0),0)
	
	def test_checkone(self):
		self.assertEqual(summation(1),1)

	def test_first_five(self):
		self.assertEqual(summation(1),1)	
		self.assertEqual(summation(2),3)
		self.assertEqual(summation(3),6)		
		self.assertEqual(summation(4),10)
		self.assertEqual(summation(5),15)

	def test_negative(self):
		with self.assertRaises(Exception):
			summation(-1)	
		# self.assertTrue(len('xyz') == 3)
		# self.assertEqual(len('xyz'),3)
		# self.assertFalse()
		# self.assertNone(expression)
		# self.assertNotEqual(x,y)
		# self.assertNotNone(expression)

		def test_big_number(self):
			self.assertEqual(sumamation(123456879678567867867867453492340125),0)
	# check out the docs for full unit test assertions
	#output only gets output if it fails. See UnitTest 2
	# not limited to one class
	# setUp, tearDown, 
if __name__ == '__main__':
	unittest.main()