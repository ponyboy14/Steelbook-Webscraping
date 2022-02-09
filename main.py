from bs4 import BeautifulSoup
import requests as rq
import numpy as np


def bszavvi():
  # get number of pages on website
	zavvi = rq.get('https://us.zavvi.com/offers/steelbooks.list?search=Steelbook&pageNumber=1').text
	zsoup = BeautifulSoup(zavvi, 'lxml')
	pages = zsoup.find('a', class_='responsivePaginationButton--last').text.replace(' ','').strip()
  # loop through all pages
	for i in range(int(pages)):
		print(f'Page: {str(i+1)}')
		zavvi = rq.get(f'https://us.zavvi.com/offers/steelbooks.list?search=Steelbook&pageNumber={str(i+1)}').text
		zsoup = BeautifulSoup(zavvi, 'lxml')
    #find all steelbooks on page
		cases = zsoup.find_all('li', class_='productListProducts_product')
    # loop though all the steelbooks on page
		for case in cases:
			button = case.find('div', class_='productBlock_actions').text.strip().split(' ')
      # print if it is not sold out
			if(button[0] == 'Quick' or button[0] == 'Pre-order'):
				name = case.find('h3', class_='productBlock_productName').text.strip()
				price = float(case.find('span',class_='productBlock_priceValue').text.strip()[1:])
				print(f'Name: {name}')
				print(f'Price: {price}\n')

def bsblu():
  # get number of pages on website
	blu = rq.get('https://www.bluraysforeveryone.com/category-s/103.htm?searching=Y&sort=4&cat=103&show=30&page=1').text
	bsoup = BeautifulSoup(blu, 'lxml')
	pages = bsoup.find('input', attrs={"title": "Go to page"}).parent.text.split()[-1]
	# loop through all pages finding all available steelbooks
	for i in range(int(pages)):
		blu = rq.get(f'https://www.bluraysforeveryone.com/category-s/103.htm?searching=Y&sort=4&cat=103&show=30&page={str(i+1)}').text
		bsoup = BeautifulSoup(blu, 'lxml')
    # delete all steelbooks without a price
		gone = bsoup.find_all('div', class_='product_subtext')
		for t in gone:
			t.parent.parent.parent.parent.parent.decompose()
    # find all remaining steelbooks on the page
		cases = bsoup.find_all('div', class_='v-product')
		print(f'Page {i+1}')
		# loop through the steelbooks on current page
		for case in cases:
			if(case.find('div', class_='product_productprice') != 'NoneType'):
				price = case.find('div', class_='product_productprice').b.text.split()[-1]
				name = case.find('a', class_='colors_productname').text
				print(f'Name: {name}')
				print(f'Price: {price}\n')


if __name__ == '__main__':
	bsblu()
	bszavvi()
