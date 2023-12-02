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
				if int(n) > 14:
					f = 0
			if j.endswith('green'):
				n,k = list(j.split())
				if int(n) > 13:
					f = 0
			if j.endswith('red'):
				n,k = list(j.split())
				if int(n) > 12:
					f = 0
		# print(i,":",w)
	if f == 1:
		game.append(int(list(g.split())[-1]))
print(sum(game))
				