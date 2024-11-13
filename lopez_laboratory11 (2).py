word_count=0
words=[]
matched_words=[]
while word_count<10:
    word=input("enter a word:")
    words.append(word)
    word_count+=1
num=int(input("enter the number of letters:"))
for i in words:
    if len(i)>=num:
        matched_words.append(i)
print(matched_words)