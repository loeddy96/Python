print("作業(1)")
n1=int(input("請輸入第一個數字"))
n2=int(input("請輸入第二個數字"))
op=int("請選擇運算方式(+,-,*,/)")
if op=="+":
    print(n1,op,n2,"=",n1+n2)
elif op=="-":
    print(n1,op,n2,"=",n1-n2)
elif op=="*":
    prit(n1,op,n2,"=",n1*n2)
elif op=="/":
    print(n1,op,n2,"=",n1/n2)
else :
    print("請輸入有效符號")
print("作業(2)")
n=int(input("請輸入一個正整數"))
x=n**0.5
if x%1==0:
    print(n,"的平方根為",x)
else:
    print("此正整數沒有平方根")
print("作業(3)")
for x in range(1,10):
    for y in range(1,10):
print(x,"x",y,"="x*y)

