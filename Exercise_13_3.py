Import string, time

def punctuation(item):

	punctuation = string.punctuation

	for c in item:

		if c in punctuation:

			item=item.replace(c,’’)

	return item

def break_into_words():

	myfile=opne(“words.txt”,”r”)

	words_list=[]

	for line in myfile:

		for item in line.strip():

			item=punctuation(item)

			item=item.lower()

			words_list.append(item)

	return words_list
