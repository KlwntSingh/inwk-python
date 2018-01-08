def draw_grid(rows, columns):
	for i in range(5* rows + 1):
		if i % 5 == 0:
			for j in range(5* columns + 1):
				if j % 5 == 0:
					print "+",
				else:
					print "-",
			print
		else:
			for j in range(5* columns + 1):
				if j % 5 == 0:
					print "|",
				else:
					print " ",
			print




draw_grid(5,5)
