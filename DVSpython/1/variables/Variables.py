# syntax:<variable name> = <value>
# import time
# a = 10
# time.sleep(1000)

anInt = 10
aFloat = 10.25
aString = "Be Optimistic"
aBool = True
aBoolean = False

# chained Assignment
a = b = c = d = 2
print(a)
print(b)
print(c)
print(d)

print('**a:',a,'**b:',b,'**c:',c,'**d:',d)
print('**a:'+str(a),'**b:'+str(b),'**c:'+str(c),'**d:'+str(d))
print("**a:{} **b:{} **c:{} **d:{}".format(a,b,c,d))
print(f"**a:{a} **b:{b} **c:{c} **d:{d}")

# Multi Assignment
a,b,c = 100,200,300
print(a)
print(b)
print(c)

a = 20
print(type(a))

print(type(anInt))
print(type(aFloat))
print(type(aString))
print(type(aBool))

# returns size of object in bytes
print(anInt.__sizeof__())
print(aFloat.__sizeof__())
print(aString.__sizeof__())
print(aBool.__sizeof__())






