words = ['Thirty','Days','Of','Python']
result = ' '.join(words)
print(result)
---> Thirty Days Of Python

words = ['Coding', 'For' , 'All']
result = ' '.join(words)
print(result)
---> Coding For All

company = "Coding For All"

print(company)
---> Coding For All

company = "Coding For All"
print(len(company))
---> 14

company = "Coding For All"
print(company.upper())
---> CODING FOR ALL
company = "Coding For All"
print(company.lower())
---> coding for all

company = "Coding For All"
print(company.capitalize())
print(company.title())
print(company.swapcase())
---> Coding for all
Coding For All
cODING fOR aLL

company = "Coding For All"
word = company[:6]
print(word)
---> Coding

# method 1
string = "Coding For All"
sub_string = 'Coding'
print(string.index(sub_string))
---> 0
# method 2
string = "Coding For All"
text = string.find('Coding')
print(text)

string = "Coding For All"
text = string.replace('Coding','Python')
print(text)
---> Python For All

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
string = '#'.join(libraries)
print(string)
---> Django#Flask#Bottle#Pyramid#Falcon

print("I am enjoying this challenge.\nI just wonder what is next.")
---> I am enjoying this challenge.
I just wonder what is next.

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
---> Name    Age     Country City
Asabeneh        250     Finland Helsinki

radius = 10
area = 3.14 * radius ** 2
string='radius = {}'.f
string='The area of a circle with radius {} is {} meters square.'.format(radius,area)
print(string)
---> The area of a circle with radius 10 is 314.0 meters square.

a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
---> 8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
