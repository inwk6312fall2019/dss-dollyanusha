def markov(lett, n):
	if lett.isupper():
		start = ord("A")
	elif lett.islower():
		start=ord("a")
	else:
		start=ord(lett)

	lett_chr = ord(lett)
	diff = strat+((lett_chr-strart)+n)%26
	print(chr(diff))

