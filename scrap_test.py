import sys
import requests
from BeautifulSoup import BeautifulSoup
import re
import unittest

class cr:
    def __init__(self):
        pass

    def productNameCleaner(self,name):
        pass

        
    def pageKeywordSearch(self,keyword,pageNo):
        url = "http://www.shopping.com/products~PG-" + pageNo + "?KW=" + keyword
        response = requests.get(url)
        data = response.content
        productString = ""
        try:
            soup = BeautifulSoup(data)
            productName = soup.findAll(id=re.compile('nameQA.*'))
            for product in productName:
                productString += (product.get('title')) + '\n'
            results = soup.findAll('span',{'class':'numTotalResults'})
            m = re.search('(of )([0-9]+)',str(results[0].contents))
            productString = productString + ( m.group(2))
            return productString
        except Exception as e:
            print e


    def keywordSearch(self,keyword):
        url = "http://www.shopping.com/products?KW=" + keyword
        response = requests.get(url)
        data = response.content
        try:
            soup = BeautifulSoup(data)
            results = soup.findAll('span',{'class':'numTotalResults'})
            m = re.search('(of )([0-9]+)',str(results[0].contents))
            return m.group(2)
        except Exception as e:
            print e
#unit test will run two test cases one for each function in cr class 'crawler class'
class MyTest(unittest.TestCase):
    
    def testOne(self):
        obj = cr()
        self.assertEqual(obj.keywordSearch("drill"),"1500")
        
    def testTwo(self):
        obj = cr()
        fp = open('test','r')
        # using common unit testing method. Trying to write mock code
        self.assertEqual(obj.pageKeywordSearch("drill","2"),fp.read())

unittest.main()

