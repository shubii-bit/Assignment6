

X = [[5000,10000,6000],
	[20000,10000,10000]]
y=0.02
result = [[0,0,0],
		[0,0,0]]

# iterate through rows
for i in range(len(X)):
# iterate through columns
	for j in range(len(X[0])):
		result[i][j] =y* X[i][j]

for r in result:
	print(r)
