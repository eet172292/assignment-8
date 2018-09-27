
out=[]

class cross:	#class definition
	def __init__(self, data):
		self.data = data
		self.top = 0  
		self.down = 0 
		self.left = 0
		self.right = 0

x = input()			# reading the values of n,m
row = int(x.split(" ")[0])
col = int(x.split(" ")[1])

mat=[[0 for i in range(col)]for j in range(row)]

for i in range(row):
	mat[i]=input().split(" ")	#reading cross values and storing it in a matrix

for i in range(row):
    for j in range(col):	#for each element assigning data members of class
        mat[i][j]= cross(mat[i][j])


for i in range(row):
	for j in range(col):
		if(mat[i][j].data == 'S'):	#iterating loop over only smart cells
			up = i-1				#if smart cell then top will be above element
			d = i+1					#if smart cell then top will be below element
			l = j-1					#if smart cell then top will be leftmost element and starting loop
			r = j+1					#if smart cell then right will be nexr right and starting loop
			for up in range(i-1,-1,-1):
				if(mat[up][j].data != 'D'): #iterating till not getting dull cell
					mat[i][j].top=mat[i][j].top+1	#if smart cell then increment value
				else:
					break
			
			for down in range(i+1,row):
				if(mat[down][j].data != 'D'):			#iterating till not getting dull cell
					mat[i][j].down=mat[i][j].down+1		#if smart cell then increment value
				else:
					break

			for l in range(j-1,-1,-1):
				if(mat[i][l].data != 'D'):				#iterating till not getting dull cell
					mat[i][j].left=mat[i][j].left+1		#if smart cell then increment value
				else:
					break

			for r in range(j+1,col):
				if(mat[i][r].data != 'D'):				#iterating till not getting dull cell
					mat[i][j].right=mat[i][j].right+1	#if smart cell then increment value
				else:
					break

			temp=min(mat[i][j].top,mat[i][j].down,mat[i][j].left,mat[i][j].right) #finding min
			out.append(temp);

n=len(out)
out.sort()
print(out[n-1]*4+1," ",out[n-2]*4+1)	#printing largest and 2nd largest

####### write your code here ##########
