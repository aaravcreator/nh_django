print("HELLO WORLD")

a = 5
print(a)

print(type(a))

b = 5.0
print(type(b))

c = "RAM IS A GOOD MAN"
print(type(c))

print(b)
print(int(b))

z = 5.83

print(type(str(z)))



my_list = [1,2,3,4,"ram","shyam"]

print(len(my_list))

print(my_list[1])
print(my_list[-1])


items = ['p','r','o','b','e']

print(items[-1])
print(items[1:3])


a = 5
b = 10
c = 15

sum_ab = a+b
product_bc = b*c

numbers = [a,b,c]
numbers.append(sum_ab)
print(numbers)
numbers.insert(1,product_bc)
print("LIST BEFORE POP : ",numbers)
numbers.pop(0)
print("FINAL LIST: ",numbers)

numbers.sort(reverse=True)
print("SORTED: ",numbers)

# [150,15,15,10]
for num in numbers:
    print(num)
    print("INSIDE FOR")
    print("INSIDE")

print("IS ON LOOP")


person_list = []
# for i in range(1,6):
#     name = input("Enter your name: ")
    
#     # get first leter of name
#     first_letter = name[0]

#     # if first_letter == "A":
#     #     print("A")
#     # elif first_letter == "a":
#     #     print("a")
#     if first_letter.upper() == "A":
#         print("A")
#     else:
#         print("NOT A")
#         person_list.append(name)



# print(person_list)

for person in person_list:
    print(person)

# price = input("enter price:")
# product = {
#     'name':"RICE",
#     'quantity':2,
#     'price':price
# }
# product_list.append(product)

# Program to take data of 5 products [name, quantity,price] from user


product_list = []
for i in range(1,3):
    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        'name':name,
        'price':price,
        'quantity':quantity
    }
    product_list.append(product)

# printing product items
print("-----PRODUCTS----")
for product in product_list:
    print("NAME: ",product['name'])
    print("PRICE: ",product['price'])
    print("QUANTITY: ",product['quantity'])
    product_total = product['price'] * product['quantity']
    print("TOTAL: ",product_total)

















