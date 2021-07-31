car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000}
print(car_prices)
print(car_prices['toyota'])
car_prices['mazda'] = 4000
print(car_prices)
car_prices['opel'] = 2000
print(car_prices)
#удаление одного элемента
del car_prices['toyota']
print(car_prices)
#удаление всего словаря
car_prices.clear()
print(car_prices)

