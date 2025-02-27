#swap values of two variables
a= 10
b= 5
c = 20
d = 15

print(f"values before swap: a={a}, b={b}")

#using a third variable
temp = a
a = b
b = temp

print(f"Values after swapping using a third variable: a={a}, b={b}")

#without using a third variable

c,d = d,c

print(f"Values after swapping without using a third variable: c={c}, d={d}")