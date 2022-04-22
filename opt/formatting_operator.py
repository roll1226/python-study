num1 = 30
result = "10進数では %d 、16進数では %x です" % (num1, num1)
print(result)

def mypoint(str1, num1):
    result = "My name is %-10s, point is %5d." % (str1, num1)
    print(result)

mypoint("Yamada", 75)
mypoint("Sugiyama",1825)

num1 = 30
print("10進数では %d 、16進数では %x です" % (num1, num1))


name = "Suzuki"
old = 18
print("名前は%-8sです。年齢は%03d歳です。" % (name, old))

print("10進数=%d, 16進数=%x" % (20, 20))

print("指数表記=%e, 固定小数点表記=%f" % (0.0752, 0.0752))

print("10進数=%(decnum)d, 16進数=%(hexnum)x" % {"hexnum":20, "decnum":20})

print("数値1=%x, 数値2=%#x" % (30, 30))

print("数値1=%5d, 数値2=%05d" % (30, 30))

print("数値1=[%5d], 数値2=[%-5d]" % (30, 30))

print("数値1=%d, 数値2=%d, 数値3=% d, 数値4=% d" % (30, -30, 30, -30))

print("数値1=%+d, 数値2=%+d" % (30, -30))

print("数値1=%d, 数値2=%4d, 数値3=%4d" % (30, 30, 72536))

print("数値1=%d, 数値2=%*d" % (18, 5, 42))

print("数値1=%f, 数値2=%.3f" % (1/3, 1/3))

print("数値1=%f, 数値2=%.*f" % (1/3, 3, 1/3))
