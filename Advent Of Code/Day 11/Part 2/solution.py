#original matrix ----> modified matrix -----> count the # in the rows combination ----> count the path combinations column wise

with open('input2', 'r') as file:
    # Read the file line by line
    matrix = [list(line.strip()) for line in file]

print("A")

for i in matrix:
	print(i)

rows = len(matrix)
columns = len(matrix[0])

print(rows, columns)
sum = 0
count = 0
mark_col = []
mark_row = []

for i in range(rows):
	for j in range(columns):
		if matrix[i][j] == '.':
			count+= 1
	
	if count == columns:
		mark_row.append(i)
	count = 0 
print(mark_row)
		
for j in range(columns):
	for i in range(rows):
		if matrix[i][j] == '.':
			count+= 1
	
	if count == rows:
		mark_col.append(j)
	count = 0 
print(mark_col)


a = [['.'] * (columns+len(mark_col)*999999) for _ in range(rows+len(mark_row)*999999)]
print(len(a),len(a[0]))
for i in a:
	print(i)

for i in range(rows):
	for j in range(columns):
		if matrix[i][j]=="#":
			count_i = 0
			count_j = 0
			for k in mark_row:
				if i > k: 
						count_i +=999999
			for l in mark_col:
				if j > l:
					count_j +=999999
					
			print((i,k),(j,l),(count_i,count_j))
			# print((i,k),(j,l),(count_i,count_j))
			a[i+count_i][j + count_j] = "#"

# print(a)
for i in a:
	print(i)

matrix = a
rows = len(matrix)
columns = len(matrix[0])
	
for i in matrix:
	if i.count("#") > 1:
		for j in range(columns):
			if i[j] == "#":
				for k in range(j+1, columns):
					if i[k] == "#":
						sum+= abs(k-j)
for i in range(rows):
	for j in range(columns):
		if matrix[i][j] == "#":
			for k in range(i+1, rows):
				for l in range(columns):
					if matrix[k][l] == '#':
						sum += abs(k - i )+ abs(l - j)
						# print(sum, (i,j),(k,l))
print("total", sum)
