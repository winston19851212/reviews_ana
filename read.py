data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('finish reading, have:', len(data), 'lines')

print(data[0])

wc = {} 
for d in data:
	words = d.split(' ')

	for word in words:
		if word in wc:
			wc[word]+= 1
		else:
			wc[word] = 1
'''
for word in wc:
	if wc[word] > 100:
		print(word, wc[word])

print (len(wc))
'''
while True:
	word = input('what word do you want to search?:')
	if word =='q':
		
		break
	if word in wc:
		print(word, 'appeared', wc[word])

	else:
		print('we dont have this word!')

print('thank you for using')
	#print(words)
	#break




sum_len = 0
for d in data:
	sum_len += len(d)
print('the average length of the messages is ', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('total has', len(new), 'length less than 100')
print(new[0])
print (new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('total had', len(good), 'deals in the loop')
print(good[0])

good = [1 for d in data if 'good' in d]
print(good)





