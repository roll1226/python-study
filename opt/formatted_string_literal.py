name = "Suzuki"
old = 18
print("名前は{:<8}です。年齢は{:>3d}歳です。".format(name,old))
print(f"名前は{name:<8}です。年齢は{old:>3d}歳です。")
print(f"名前は{{ {name:<8s} }}です。")

num = 0.0752
print(f"指数表記={num:e}")
print(f"固定少数店表記={num:f}")
print(f"パーセンテージで表示={num:%}")

str1 = "Lemon"
print(f"文字列=[{str1:<10s}]")
print(f"文字列=[{str1:^10s}]")
print(f"文字列=[{str1:>10s}]")

num = 1234567
print(f"数値={num:,d}")
