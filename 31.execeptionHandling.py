# try:
#     print(x)
# except:
#     print('An exception is occured')

# try:
#     print(x)
# except NameError:
#     print('Varible is not defined')
# except:
#     print('somthing wrong')

# try:
#     print("hello")
# except:
#     print("somthing wrong")
# else:
#     print("Nothing went wrong")
x=1
try:
    if x<0:
       raise Exception("sorry no number below than zero")
except Exception as e:
    print(e)