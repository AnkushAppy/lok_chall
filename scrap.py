import sys
import requests
from BeautifulSoup import BeautifulSoup
import re

#crawler class
class cr:
        def __init__(self):
                pass
        def productNameCleaner(self,name):
                pass

        def pageKeywordSearch(self,keyword,pageNo):
                url = "http://www.shopping.com/products~PG-" + pageNo + "?KW=" + keyword
                #print url
                try:
                        response = requests.get(url)
                        data = response.content
                        productString = ''
                        soup = BeautifulSoup(data)
                        productName = soup.findAll(id=re.compile('nameQA.*'))
                        for product in productName:
                                productString += product.get('title') + '\n'
                        results = soup.findAll('span',{'class':'numTotalResults'})
                        m = re.search('(of )([0-9]+)',str(results[0].contents))
                        productString += m.group(2)
                        return productString
                except Exception as e:
                        return e

        def keywordSearch(self,keyword):
                url = "http://www.shopping.com/products?KW=" + keyword
                #print url
                try:
                        response = requests.get(url)
                        data = response.content
                        soup = BeautifulSoup(data)
                        results = soup.findAll('span',{'class':'numTotalResults'})
                        m = re.search('(of )([0-9]+)',str(results[0].contents))
                        return m.group(2)
                except Exception as e:
                        return e



#raw_input will take input in string format. So no need to convert.
keyword = raw_input("Enter keyword: ")
page = raw_input("Enter page number: ")
#cr object
obj = cr()
print obj.pageKeywordSearch(keyword, page)
print obj.keywordSearch(keyword)

