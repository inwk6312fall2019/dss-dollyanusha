Import random, time

def histogram(s)

	d=dict()

	for c in s:

		d[c]=d.get(cps.count(c))

	return d

def sum_values(*t):

	return sum(t)

def choose_histogram(h):

	print(h)

	key=random.choice(list(h.keys()))

	prob=h[key]/sum(h.values()]

	sum=sum(h.values())

	print(‘random value is “{}” and its probability is {}/{}, i.e. {}.’\ .format(random_key, h[random_key], sum(h.values()), probability))

start_time=time.time()

h=histogram(“aba”)

choose_histogram(h)

function_time=time.time()-strat_time

Print(‘\nrunning time is {0:.4f} s’ .formqat(function_time)) 
