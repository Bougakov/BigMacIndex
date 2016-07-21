# This Python script uses library from http://grablib.org/ 
# Use Python 3.5 to run it (https://www.continuum.io/downloads is recommended)
# If you'd run it from Windows console, don't forget to issue this command to prevent Unicode conversion errors:
# chcp 65001

# Here we set up libraries:
import logging
from grab import Grab
import csv
import datetime

# We log plenty of stuff to debug:
logger = logging.getLogger('grab')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.ERROR) # change to DEBUG if needed

# McDonalds assigns IDs to Russian cities. Moscow has code 42:
city_id = 42

# we store current date to record when price monitoring was conducted:
today = datetime.datetime.now().strftime("%Y.%m.%d %H-%M-%S")

# here we declare variables to store data we grab from McDonalds.ru pages:
product_id = 0
product_url = ""
product_name = ""
product_variant_id = ""
product_variant = ""
product_price = ""
product_description = ""
product_contents = ""
product_pic = ""
city_name = ""

# here we select cities that need to be checked. We can either check the full range or select ones. Comment out the unnecessary option
select_cities = range(71, 98) # from city with ID=2 ("Almetyevsk") to ID=98 ("Yaroslavl") 
#select_cities = [42]

# McDonalds has IDs for every product. At the time of writing max code was 96.
mcd_product_ids = range(1, 99)

# initialization:
g = Grab()
g.setup(method='get')
g.setup(connect_timeout=30)
g.setup(connect_timeout=75)
g.setup(log_file='grab.log')

# We write our results into plain text Excel file separated by TABs:
with open(('McDonalds price list ' + today + '.csv'), 'w', newline='') as csvfile:
	excelfields = ['city_id', 'city_name', 'today','product_id','product_name','product_variant_id','product_variant','product_price','product_description','product_contents','product_url','product_pic']
	writer = csv.DictWriter(csvfile, dialect='excel-tab', fieldnames=excelfields)
	writer.writeheader()
	for city_id in select_cities: # This array holds city IDs and names. I obtained it from dropdown box at McDonalds website:
		city_name = ""
		if city_id == 2: city_name = "Альметьевск"
		if city_id == 3: city_name = "Армавир"
		if city_id == 4: city_name = "Архангельск"
		if city_id == 5: city_name = "Астрахань"
		if city_id == 6: city_name = "Белгород"
		if city_id == 7: city_name = "Брянск"
		if city_id == 8: city_name = "Бугульма"
		if city_id == 9: city_name = "Великие Луки"
		if city_id == 10: city_name = "Великий Новгород"
		if city_id == 11: city_name = "Владимир"
		if city_id == 12: city_name = "Владимирская область"
		if city_id == 13: city_name = "Волгоград"
		if city_id == 14: city_name = "Волжский"
		if city_id == 15: city_name = "Вологда"
		if city_id == 16: city_name = "Воронеж"
		if city_id == 17: city_name = "Геленджик"
		if city_id == 18: city_name = "Домодедово"
		if city_id == 19: city_name = "Екатеринбург"
		if city_id == 20: city_name = "Елабуга"
		if city_id == 21: city_name = "Елец"
		if city_id == 22: city_name = "Звенигород"
		if city_id == 23: city_name = "Иваново"
		if city_id == 24: city_name = "Ижевск"
		if city_id == 25: city_name = "Йошкар-Ола"
		if city_id == 26: city_name = "Казань"
		if city_id == 27: city_name = "Калининград"
		if city_id == 28: city_name = "Калуга"
		if city_id == 29: city_name = "Киров"
		if city_id == 30: city_name = "Клин"
		if city_id == 31: city_name = "Королев"
		if city_id == 32: city_name = "Кострома"
		if city_id == 33: city_name = "Красногорск"
		if city_id == 34: city_name = "Краснодар"
		if city_id == 35: city_name = "Кстово"
		if city_id == 36: city_name = "Курск"
		if city_id == 37: city_name = "Ленинградская область"
		if city_id == 38: city_name = "Липецк"
		if city_id == 39: city_name = "Лыткарино"
		if city_id == 40: city_name = "Магнитогорск"
		if city_id == 41: city_name = "Можайск"
		if city_id == 42: city_name = "Москва"
		if city_id == 43: city_name = "Московская область"
		if city_id == 44: city_name = "Мурманск"
		if city_id == 45: city_name = "Набережные Челны"
		if city_id == 46: city_name = "Нижегородская область"
		if city_id == 47: city_name = "Нижневартовск"
		if city_id == 48: city_name = "Нижнекамск"
		if city_id == 49: city_name = "Нижний Новгород"
		if city_id == 50: city_name = "Новокузнецк"
		if city_id == 51: city_name = "Новокуйбышевск"
		if city_id == 52: city_name = "Новомосковск"
		if city_id == 53: city_name = "Новороссийск"
		if city_id == 54: city_name = "Новосибирск"
		if city_id == 55: city_name = "Новочебоксарск"
		if city_id == 56: city_name = "Обнинск"
		if city_id == 57: city_name = "Омск"
		if city_id == 59: city_name = "Оренбург"
		if city_id == 58: city_name = "Орёл"
		if city_id == 60: city_name = "Павловский Посад"
		if city_id == 61: city_name = "Пенза"
		if city_id == 62: city_name = "Пермь"
		if city_id == 63: city_name = "Петрозаводск"
		if city_id == 64: city_name = "Покров"
		if city_id == 65: city_name = "Псков"
		if city_id == 66: city_name = "Пятигорск"
		if city_id == 69: city_name = "Ростов-на-Дону"
		if city_id == 70: city_name = "Ростовская область"
		if city_id == 71: city_name = "Рязань"
		if city_id == 72: city_name = "Самара"
		if city_id == 73: city_name = "Санкт-Петербург"
		if city_id == 74: city_name = "Саранск"
		if city_id == 75: city_name = "Саратов"
		if city_id == 76: city_name = "Северодвинск"
		if city_id == 77: city_name = "Смоленск"
		if city_id == 78: city_name = "Сочи"
		if city_id == 79: city_name = "Ставрополь"
		if city_id == 80: city_name = "Старый Оскол"
		if city_id == 81: city_name = "Сургут"
		if city_id == 82: city_name = "Сызрань"
		if city_id == 99: city_name = "Сыктывкар"
		if city_id == 83: city_name = "Таганрог"
		if city_id == 84: city_name = "Тамбов"
		if city_id == 85: city_name = "Тверская область"
		if city_id == 86: city_name = "Тверь"
		if city_id == 87: city_name = "Тольятти"
		if city_id == 88: city_name = "Тула"
		if city_id == 89: city_name = "Тюмень"
		if city_id == 90: city_name = "Ульяновск"
		if city_id == 91: city_name = "Уфа"
		if city_id == 92: city_name = "Чебоксары"
		if city_id == 93: city_name = "Челябинск"
		if city_id == 94: city_name = "Череповец"
		if city_id == 95: city_name = "Чехов"
		if city_id == 96: city_name = "Энгельс"
		if city_id == 97: city_name = "Ярославль"
		if city_id == 98: city_name = "Ярославская область"
		if city_id == 67: city_name = "респ. Адыгея"
		if city_id == 68: city_name = "респ. Коми"

		# To get prices for different cities we change cookie to the required City ID:
		g.cookies.set(name='city_id', value=str(city_id), domain='mcdonalds.ru', path='/')
		for x in mcd_product_ids:
			print ('Checking https://mcdonalds.ru/products/' + str(x) + ' for city ' + str(city_id) + ' ...')
			try: 
				g.go(('https://mcdonalds.ru/products/' + str(x)), user_agent='Colonel Sanders')
			# dirty hack to make script retry failed download attempts:
			except grab.error.GrabConnectionError: 
				print ('!!! GrabConnectionError occured, retrying...')
				time.sleep(10) # delays for 5 seconds
				g.go(('https://mcdonalds.ru/products/' + str(x)), user_agent='Colonel Sanders')
			except grab.error.GrabTimeoutError:
				print ('!!! GrabTimeoutError occured, retrying...')
				time.sleep(10) # delays for 5 seconds
				g.go(('https://mcdonalds.ru/products/' + str(x)), user_agent='Colonel Sanders')
			if int(g.response.code) == 200: # we only parse response if mcdonalds.ru responds with code "200". If it returns ERROR 404, we skip
				if g.doc.text_search(u'product__show-tabs'): # some McDonalds products have varieties, such as Coke 0.2L, 2.3L and 0.5L. We read HTML code to check for that:
					print ('  There are several varieties of product ' + str(x) + ' .')
					for v in range(0, 4):
						try:
							product_id             = str(x)
							# we analyze the DOM of HTML page to reach the text fragments we need. To find the required piece of HTML, open mcdonalds.ru in Google Chrome, 
							# click the page element and hit "Inspect". Find the corresponding part of HTML code and select "Copy XPath" 
							product_name           = g.xpath_text('/html/body/div[1]/main/div[1]/div/div/div/div[1]/h1')
							product_variant_id	   = str((v + 1))
							product_variant        = g.xpath_text('/html/body/div[1]/main/div[1]/div/div/div/div[1]/div[1]/ul/li[' + str(v + 1) + ']/button/span')
							product_price	       = g.xpath_text('//*[@id="tab-product_price-' + str(x) + '-' + str(v) + '"]/h4')
							product_price	       = product_price.replace(" рубль*", "", 1) # we strip currency symbol leaving only digits
							product_price	       = product_price.replace(" рубля*", "", 1)
							product_price	       = product_price.replace(" рублей*", "", 1)
							if product_price == "": product_price = "?"
							product_description    = g.xpath_text('/html/body/div[1]/main/div[1]/div/div/div/div[3]/div[1]')
							product_description    = product_description.replace("Показать", "", 1) # some minor cleanup of the values
							product_description    = product_description.replace("Скрыть", "", 1) 
							product_description    = product_description.replace("Состав и пищевую ценность", "", 2)
							product_contents	   = g.xpath_text('//*[@id="collapse--composition"]/div')
							product_pic		       = g.xpath('//*[@id="tab-product-' + str(x) + '-' + str(v) + '"]/img/@src')
							writer.writerow(
								{
									'city_id':             str(city_id), 
									'city_name':           city_name, 
									'today':               today, 
									'product_id':          product_id, 
									'product_name':        product_name, 
									'product_variant_id':  product_variant_id, 
									'product_variant':     product_variant, 
									'product_price':       product_price, 
									'product_description': product_description, 
									'product_contents':    product_contents.rstrip(),
									'product_url':         ('https://mcdonalds.ru/products/' + str(x) + '?city_id=' + str(city_id)),
									'product_pic':         ('https://mcdonalds.ru' + product_pic)
								}
							)
						except IndexError:
							product_variant = "null"
				else:
					print ('  There is a single variety of product ' + str(x) + ' .')
					product_id             = str(x)
					product_name           = g.xpath_text('/html/body/div[1]/main/div[1]/div/div/div/div[1]/h1')
					product_variant_id	   = ""
					product_variant	       = ""
					product_price	       = g.xpath_text('//*[@id="tab-product_price-' + str(x) + '-0"]/h4')
					product_price	       = product_price.replace(" рубль*", "", 1) # we strip currency symbol leaving only digits
					product_price	       = product_price.replace(" рубля*", "", 1)
					product_price	       = product_price.replace(" рублей*", "", 1)
					product_description    = g.xpath_text('/html/body/div[1]/main/div[1]/div/div/div/div[3]/div[1]')
					product_description    = product_description.replace("Показать", "", 1) # some minor cleanup of the values
					product_description    = product_description.replace("Скрыть", "", 1) 
					product_description    = product_description.replace("Состав и пищевую ценность", "", 2)
					product_contents	   = g.xpath_text('//*[@id="collapse--composition"]/div')
					product_pic		       = g.xpath('//*[@id="tab-product-' + str(x) + '-0"]/img/@src')
					writer.writerow(
						{
							'city_id':             str(city_id), 
							'city_name':           city_name, 
							'today':               today, 
							'product_id':          product_id, 
							'product_name':        product_name, 
							'product_variant_id':  product_variant_id, 
							'product_variant':     product_variant, 
							'product_price':       product_price, 
							'product_description': product_description, 
							'product_contents':    product_contents.rstrip(),
							'product_url':         ('https://mcdonalds.ru/products/' + str(x) + '?city_id=' + str(city_id)),
							'product_pic':         ('https://mcdonalds.ru' + product_pic)
						}
					)
				# let's erase variables to ensure that the next iteration starts from scratch:
				product_id = 0
				product_url = ""
				product_name = ""
				product_variant_id = ""
				product_variant = ""
				product_price = ""
				product_description = ""
				product_contents = ""
				product_pic = ""
			else:
				print ('Cant not find product with ID ' + str(x) + ' !')

