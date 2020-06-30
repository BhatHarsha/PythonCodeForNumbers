
while True:
	n=input('Number')
	break
n=int(n)
a=n
b=n*100
while True:
    num = input("Enter a number: ")
    try:
        num=int(num)
        if num>a:
    		a=num
        elif num<b:
            b=num
    except:
        print('Invalid input')
    
    if num == "done" : break
print("Maximum is",a )
print('Minimum is',b)