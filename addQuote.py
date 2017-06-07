
source = raw_input('Source: ')
quote = raw_input('Quote: ')

with open('/Users/joshnorton/python/quoteProject/quotes.txt','a') as file:
	line = "\n" + source + '|"'+quote+'"'
	file.write(line)

print 'Added :' + line
