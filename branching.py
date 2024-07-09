

person_list = [
    {
        'name':"RAM",
        'age':24,
        'gender':"M"
    },
    {
        'name':"SHYAM",
        'age':30,
        'gender':"M"
    },
    {
        'name':"GITA",
        'age':14,
        'gender':"F"
    },
]

import time


for index , person in enumerate(person_list,):
    print(index)
    if person['age'] >=18:
        print("ADULT: ")
        print("NAME: ",person['name'], "AGE: ",person['age'],'GENDER : ',person['gender'])
    else:
       print("MINOR : ")
       print("NAME: ",person['name'], "AGE: ",person['age'],'GENDER : ',person['gender'])
    time.sleep(4) # delays by 4 seconds

