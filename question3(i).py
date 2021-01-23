

X = [[10000,20000,30000],
	[50000,30000,10000]]

Y = [[5000,10000,6000],
	[50000,10000,10000]]


result = [[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)):
# iterate through columns
	for j in range(len(X[0])):
		result[i][j] = X[i][j] + Y[i][j]

for r in result:
	print(r)
