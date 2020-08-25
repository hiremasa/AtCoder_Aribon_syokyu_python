a=input()
A = int(a[0])

for flag in range(2**3):
	op=[]
	temp_a=A
	for i in range(3):
		if (flag>>i)&1==1:
			op.append("+")
			temp_a+=int(a[i+1])
		else:
			op.append("-")
			temp_a-=int(a[i+1])
	if temp_a==7:
		print("{}{}{}{}{}{}{}=7".format(a[0],op[0],a[1],op[1],a[2],op[2],a[3]))
		exit()
