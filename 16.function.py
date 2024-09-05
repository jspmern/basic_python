# def sum_of_number(list):
#     total=0
#     for x in list:
#         total += x
#     print(total)
# sum_of_number([1,2,3,4,5,6,7])

# def Cal_Avg_No(list=0):
#     avg=0
#     count=0
#     sum=0
#     for x in list:
#         sum +=x
#         count +=1 
#     avg=sum/count
#     return int(avg)
# result=Cal_Avg_No([2,3,4])
# print(result)      

# def check_armstrong(no):
#     print(no)
#     temp=no
#     sum=0
#     while(temp>0):
#         rem=temp%10
#         sum+=rem**3
#         temp=int(temp/10)
#     if sum==no : return True
#     else:return False

# print(check_armstrong(153))