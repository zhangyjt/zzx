# 某商店为促销推出如下让利促销方案，其中m为购买金额，n为让利百分比。
# m<100,	      n=0
# 100<=m<200,	n=2.5%
# 200<=m<300,	n=3.5%
# 300<=m<500,	n=4.5%
# 500<=m,    	n=6%
# 要求：从键盘输入顾客的购买金额，输出实际支付的金额和返还的金额（保留2位小数）。
m=eval(input("请输入你的购买金额:"))
if m<100:
	n=0
elif 100<=m<200:
	n=0.025
elif 200<=m<300:
	n=0.035
elif 300<=m<500:
	n=0.045
else:
	n=0.06
pay=m*(1-n)
re=m*n
print("用户实际支付金额{:.2f}".format(pay),"返还金额{:.2f}".format(re))


