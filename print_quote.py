import random, textwrap

with open('/Users/joshnorton/python/quoteProject/quotes.txt','r') as file:
	names = []
	quotes = []
	for line in file:
		try:
			names.append(line.split('|')[0])
			quotes.append(line.split('|')[1])
		except Exception:
			pass
name_quote_map = zip(names, quotes)
random.shuffle(name_quote_map)

indicies = [i for i in range(0, len(names)-1)]
random.shuffle(indicies)
n = indicies[0]


s = name_quote_map[n][1] + "-" +  name_quote_map[n][0]
print textwrap.fill(s)
