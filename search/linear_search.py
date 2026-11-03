def linear_search(data,search):
    for i in range(len(data)):
        if data[i] == search:
            return i
    return -1

data= [10,20,30,40,50]
search = int(input("enter data:"))

result = linear_search(data,search)
print(data)

if result == -1 :
    print("data not found")
else:
    print("data found at index:",result)
    
