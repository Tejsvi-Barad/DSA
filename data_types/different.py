list = [1,2,3,4,5]

tuple = (1,2,3,4,5)

set = {1,2,3,5,2,4}

dict = {"name":"tejsvi","age":20}

print(list)
print(tuple)
print(set)
print(dict)
print("--------------------------------------------------------------")


list = [1,2,3,4,5,6,7,8,9,10,25,0,-1,23,28]
list.append(12)
print("after add",list)

list.remove(5)
print("after remove ",list)

print(len(list))
list.sort()
print(list)

list.sort(reverse=True)
print(list)

list1 = [1,2,3,4,5]
list1.clear()
print(list1)

print("-----------------")

tuple =(1,2,3,4,5,6,7)
print(tuple)
print("-----------------")

dict = {"name": ["maya","mmet","tejsvi","barad"],
        "age": [10,29,20,38],
        "city": ["rajkot","surat","ahmdabad","mayanagri"]
        }
print(dict)

print(dict.keys())
print(dict.values())
print(len(dict))
print("-----------------")


set = {1,2,3,2,4,5,4,6,7,7,8,9,10}
print(set)
