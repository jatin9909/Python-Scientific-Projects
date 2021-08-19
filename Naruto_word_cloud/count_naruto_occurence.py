#get file object reference to the file

file = open("clean_transcript.txt", "r", encoding="utf8")
#read content of file to string
data = file.read()
#get number of occurrences of the substring in the string
i = "Believe"
occurrences = data.count(i)
print('Number of occurrences of the word ', i ,":", occurrences)