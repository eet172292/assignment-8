
def rotate(l, n):			#Function to rotate the list
    return l[-n:] + l[:-n]

k=input()					#Taking input from user
k1=int(k.split(" ")[0])
k2=int(k.split(" ")[1])
k3=int(k.split(" ")[2])
encrypt=input()

list1=['a','b','c','d','e','f','g','h','i']	# defining 3 list for each group
list2=['j','k','l','m','n','o','p','q','r']
list3=['s','t','u','v','w','x','y','z','_']
out=[]

list4=[]
list5=[]
list6=[]
for i in range(len(encrypt)):		#reading the input character by character
	#print(encrypt[i])
	if encrypt[i] in list1:	#checking character belongs to which list, accordingly adding it
		list4.append(encrypt[i])
	if encrypt[i] in list2:
		list5.append(encrypt[i])
	if encrypt[i] in list3:
		list6.append(encrypt[i])


list4=rotate(list4,k1)			#list rotated
list5=rotate(list5,k2)
list6=rotate(list6,k3)

l1=0
l2=0
l3=0

for i in range(len(encrypt)):	
	if encrypt[i] in list1:		#checking if character belongs to list1
		#print(list4[l1])
		out.append(list4[l1])	#if yes then appending rotated char value
		l1=l1+1					#Incrementing the value of counter to access the elemnet of rotated list
		#print("l1",l1)
	if encrypt[i] in list2:		#checking if character belongs to list2
		#print(list5[l2])
		out.append(list5[l2])	#if yes then appending rotated char value					
		l2=l2+1					#Incrementing the value of counter to access the elemnet of rotated list
		#print("l2",l2)
	if encrypt[i] in list3:		#checking if character belongs to list3
		#print(list6[l3])
		out.append(list6[l3])	#if yes then appending rotated char value
		l3=l3+1					#Incrementing the value of counter to access the elemnet of rotated list
		#print("l3",l3)

for i in range(len(out)):
	print(out[i],end="")
###### write your code here ##########
