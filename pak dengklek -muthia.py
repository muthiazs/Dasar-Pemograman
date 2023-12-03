s= int(input())

x=int(s/3600)
y=int((s%3600)/60)
z=int(((s%3600)%60))

print(x)
print(y)
print(z)