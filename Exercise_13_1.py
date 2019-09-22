from string import punctuation, whitespace

myfile=open(“words.txt”,’r’)

word=line.strip()

def w1(word):

	clear=‘’

	for letter in word:

		if ((char in punctuation) or (char in whitespace)):

			pass

		else:

			clear= clear+letter.lower()

	return clear

print(word)
