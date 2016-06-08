#hash code
import unittest
def hash(s):
	h = 7
	letters = "acdegilmnoprstuw"
	for i in range(len(s)):
		h = h*37 + letters.index(s[i])
	return h

def rev_hash(s):
        letters = "acdegilmnoprstuw"
        strHash = ''
        try:
                while(s > 7):
                        index = s % 37
                        strHash = letters[index] + strHash
                        s = s // 37
                return strHash
        except Exception as e:
                return "Enter valid number"

#s = raw_input("enter the word")
#lawnmower, acdegilmnoprstuw, 680131659347, 930846109532517
##s = "lawnmower"
##print hash(s)
##s="leepadg"
##print hash(s)
##s = "acdegilmnoprstuw"
##print hash(s)

class MyTest(unittest.TestCase):

	def testOne(self):
		self.assertEqual(rev_hash(680131659347),'leepadg')


	def testTwo(self):
		self.assertEqual(rev_hash(930846109532517),'lawnmower')


unittest.main()
