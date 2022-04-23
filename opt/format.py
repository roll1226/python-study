name = "Suzuki"
old = 18
print("名前は{:<8s}です。年齢は{:>3d}歳です。".format(name, old))

print("名前{:8s}です。{:4d}歳。".format("Yamada", 18))

print("名前{0:8s}です。{1:4d}歳。".format("Honda", 32))

print("名前{name:8s}です。{old:4d}歳。".format(name="Tanaka", old=24))

print("文字列={:s}, 文字列={}".format("Lemon", "Apple"))

print("数値1={:d}, 数値2={:x}".format(20, 31))

print("指数表記={:e}".format(0.0752))

print("固定小数点表記={:f}".format(0.0752))

print("パーセンテージで表示={:%}".format(0.348))

print("文字列=[{:10s}]".format("Lemon"))

print("数値=[{:5d}]".format(123))

print("数値=[{:<7d}]".format(123))

print("数値=[{:^7d}]".format(123))

print("数値=[{:>7d}]".format(123))

print("数値={:*<7d}".format(123))

print("数値={:-^7d}".format(123))

print("正の数={:+d}, 負の数={:+d}".format(72, -72))

print("正の数={:-d}, 負の数={:-d}".format(72, -72))

print("正の数={: d}, 負の数={: d}".format(72, -72))

print("数値={:,d}".format(1234567))

print("数値={:,f}".format(12345.6789))

print("数値={:_d}".format(1234567))

print("数値={:f}".format(1.2345))

print("数値={:.1f}".format(1.2345))

print("数値={:.3f}".format(1.2345))

print("数値={:b}, 数値={:#b}".format(10, 10))

print("数値={:o}, 数値={:#o}".format(20, 20))

print("数値={:x}, 数値={:#x}".format(35, 35))

