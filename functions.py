

def greet_me():
    print("HELLO !")

greet_me()


def add(a,b):
    result = a+b
    print(result)

add(5,6)

# return a+b
def calculate_sum(a,b):
    return a+b

sum_result = calculate_sum(6,8)
print(sum_result)
print(calculate_sum(6,10))


def divide(a,b):
    try:
        result = a/b
    except Exception as e :
        print(e)
        result = "CANT divide with zero"
    return result

print(divide(5,0))

def greet_person(firstName,lastName):
    print("HELLO ", firstName , " ", lastName)

greet_person(lastName="SHARMA",firstName="RAM")


def get_all(*args):
    # print(args)
    # print(args[0])
    # print(args[1])

    for item in args:
        print(item)
    

get_all(1,2,3,4,5,6,7)

def summer(*args):
    result = 0
    for num in args:
        result = result + num
    return result

print("SUM IS :",summer(1,2,3,98,44))



