def find_long_word (words_str):
	length=[]
	for n in words_str:
	     length.append((len(n), n))
	length.sort()
	return length[-1][1]

demo=["yellow","red","green"]
demo2=find_long_word(demo)
print(demo2)
