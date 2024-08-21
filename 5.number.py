# Python Numbers
# There are three numeric types in Python:

# int (unlimited length)
a=123333
#print(a,type(a))
# float
b=2.333   #e represent power of 10
#print(b,type(b))
c=2.333333333333333333333
#print(c,type(c))
# complex   #here j represent imganary part
d=2+4j
#print(d,type(d))

# Note 👉  you can convert one type to another (but complex is not convert into  another type ) and this concept known as casting
#example -1
x=5
#convert into float
y=float(x)
print(y,type(y))
#convert into complex
z=complex(x)
print(z,type(z))

#example -2
t=5.002
q=int(t)
r=complex(t)
print(q,type(q))
print(r,type(r))

#example -3
n=3+1j
s=int(n)
# print(s,type(s))   //error


