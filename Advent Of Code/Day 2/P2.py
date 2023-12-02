game = []

for i in range(100):
	g, a = list(input().split(':'))
	s = list(a.split(';'))
	
	blue = 0
	red = 0
	green = 0 
	f = 1
	for i in s:
		w = list(i.split(','))
		for j in w:
			j.strip()
			# print()
			if j.endswith('blue'):
				n,k = list(j.split())
				blue = max(blue,int(n))
			if j.endswith('green'):
				n,k = list(j.split())
				green = max(green,int(n))
			if j.endswith('red'):
				n,k = list(j.split())
				red = max(red,int(n))
		# print(i,":",w)
	game.append(blue*green*red)
print(sum(game))
