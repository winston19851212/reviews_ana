data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))
print('finish reading, have:', len(data), 'lines')

sum_len = 0
for d in data:
	sum_len += len(d)
print('the average length of the messages is ', sum_len/len(data))


