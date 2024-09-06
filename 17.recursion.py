def reverse_print(no):
    if(no==1): return
    print(no)
    reverse_print(no-1)
    
reverse_print(7)