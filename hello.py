

list1=[1,3,5,7,9,2,4,6,8]

num = 9

# for i in list1:
#     if i == num:
#         print("number exists")
#     else:
#         print("number doesnt exist")


# def search(num):
#     for i in list1:
#         if i == num:
#             return True
#     return False


# isExist = search(num)  # true or false

# if isExist:
#     print("Number Exists")
# else:
#     print("Number doesnt exist")

def search(num):
    for i in list1:
        if i==num:
            return True
    return False 

if search:
    print("Number Exist")
else:
    print("Number does not Exist")