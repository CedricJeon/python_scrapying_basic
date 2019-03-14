from bs4 import BeautifulSoup

fp = open("cars.html", encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')

def car_function(selector):
    print("car_function", soup.select_one(selector).string)

car_lambda = lambda q : print("car_lambda", soup.select_one(q).string)

car_function("#gr")
car_function("li#gr")
car_function("ul > li#gr")
car_function("#cars #gr")
car_function("#cars > #gr")
car_function("li[id='gr']")

print("car_function", soup.select("li")[3].string)
print("car_function", soup.find_all("li")[3].string)

car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul > li#gr")
car_lambda("#cars #gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")
