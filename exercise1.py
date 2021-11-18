try:
	file1=open('brown.txt')
except:
	print('File cannot be opened:', file1)
	exit()
lines=file1.readlines()
file1.close()
dict={}
file2=open('output.txt','w')

for line in lines:
	words=line.split()
	length=len(words)

	for i in range(length-1):
		key=words[i]+' '+words[i+1]
		if key not in dict:
			dict[key]=1
		else:
			dict[key]+=1

max=None
for key in dict:
	result=key,dict[key]
	file2.write(str(result))
	file2.write('\n')
	if max is None or dict[key]>max:
			max=dict[key]
print('max:',max)


#print('Average:',ave, '\nSumma:',sum, '\nDlina dict:',len(dict))
