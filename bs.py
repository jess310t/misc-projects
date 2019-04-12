from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

# The current code is specifically for kitchenaid stand mixer -- I finally got one
url = 'https://www.walmart.com/search/?cat_id=0&query=kitchenaid+stand+mixer'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#By inspecting the webpages, found tha the names of the listed products are in
# class "product-title-link line-clamp line-clamp-2" in this search result webpage
# title="" or aria-label ="" and it all rests in 'a'anchor

#istrue = True #testing loop avoid forever loop
# while istrue:

productlist = []
nameboxes = soup.find_all('a', attrs={'class':'product-title-link line-clamp line-clamp-2'})
for name in nameboxes:
    productlist.append(name.get('title',None))

pricelist = []
priceblocks = soup.find_all('div', attrs={'class':'price-main-block'})
for block in priceblocks:
    price=block.find('span', attrs={'class': 'price-group'})
    pricelist.append(price.get('aria-label', None))

# for product in productlist:
     # print(product)
# for price in pricelist:
    # print(price)
if len(pricelist) == len(productlist):
    mixerprices = dict(zip(productlist,pricelist))

# Sort the product-price pair according to price (although string prices)
priceprod = [(price,product) for product, price in mixerprices.items()]
priceprod.sort()
for pair in priceprod:
    print(pair[1])
    print(pair[0])


#Retrieve all the anchor tags
# tags = soup('a')
#print cleaned up? version of the webpage
# print(soup.prettify())
#prices = soup.findall('span')
# for line in soup.strings:
#     print(repr(line))
