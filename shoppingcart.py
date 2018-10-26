print("we have only electronics")
count=0
x=[]
y=[]
a="electronics"
k= input()
if(k==a):
	n="mobiles"
	m="t.v's"
	q=input()
	if(q==n):
		print("you entered in mobbiles list")
		g=["apple","samsung","mi","vivo","oneplus"]
		print("mention in which company do u want")
		for i in range(0,5):
			print(g[i])
		y=input()
		if(y=="apple"):
			print ("its cost is 70,000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append("70000")
				x.append("apple")
				print(y)
				print(x)
				count=count+1
		if(y=="samsung"):
			print("its cost is 50000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append(50000)
				x.append("samsung")
				print(x)
				print(y)
				count=count+1
		if(y=="mi"):
			print("its cost is 10000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append(10000)
				x.append("mi")
				print(x)
				print(y)
				count=count+1
		if(y=="vivo"):
			print("its cost is 20000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append(20000)
				x.append("vivo")
				print(x)
				print(y)
		if(y=="oneplus"):
			print("its cost is 35000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append(35000)
				x.append("oneplus")
				print(x)
				print(y)
print("do u want see t.v's")
if(q==m):
		print("you entered in mobbiles list")
		l=["apple","samsung","sony","bravia"]
		print("mention in which company do u want")
		for i in range(0,5):
			print(l[i])
		y=input()
		if(y=="apple"):
			print ("its cost is 70,0000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append(700000)
				x.append("apple")
				print(y)
				print(x)
				count=count+1
		if(y=="samsung"):
			print("its cost is 500000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append(500000)
				x.append("samsung")
				print(x)
				print(y)
				count=count+1
		if(y=="sony"):
			print("its cost is 100000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append(100000)
				x.append("sony")
				print(x)
				print(y)
				count=count+1
		if(y=="bravia"):
			print("its cost is 200000")
			print("do u want to add this cart")
			u=input()
			if(u=="yes"):
				y.append(200000)
				x.append("bravia")
				print(x)
				print(y)
				count=count+1
for j in range(count):
	

		
