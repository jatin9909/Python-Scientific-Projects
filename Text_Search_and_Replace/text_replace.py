# import all necessary modules
import re
import string
import numpy as np

#Remove formatting text
sentence = "Hi, My name is Jatin and I like to Eat Jatin's purple chocolate"
regex_name = re.compile('Jatin')
print(regex_name.findall(sentence)) #output - ['Jatin', 'Jatin']

#substitution
print(regex_name.sub('Jatin Sharma', sentence)) #Output- Hi, My name is Jatin Sharma and I like to Eat Jatin Sharma's purple chocolate

names = ['Adam','Bob','Carlos']
for name in names:
	print(regex_name.sub(name,sentence))
#Output - Hi, My name is Adam and I like to Eat Adam's purple chocolate
#         Hi, My name is Bob and I like to Eat Bob's purple chocolate
#         Hi, My name is Carlos and I like to Eat Carlos's purple chocolate

# searching with wildcards	
sentence1 = "Hi, My name is Jatin and I like to Eat Jptin's purple chocolate"
regex_name=re.compile('J\wtin')
print(regex_name.findall(sentence1)) #Output - ['Jatin', 'Jptin']


# I have a file name captions_text given in this folder in which there is a pattern given below, which I will replace. \d is for integers and \n is for new line
pattern2replace = '\\n\\n\d{1,3}\\n\d\d:\d\d.\d\d\d --> \d\d:\d\d.\d\d\d\\n' #{1,3} so that all intergers having length from 1 to 3 will included in expression
with open("captions_text.vtt","r") as rfile:
 	s=rfile.read() #reading the file

regex_timestamps = re.compile('%s'%pattern2replace)
print(regex_timestamps.findall(s)) 	 #all pattern will be print which we have to replace e.g. - ['\n\n0\n00:00.760 --> 00:05.080\n',........]

newtext = regex_timestamps.sub(' ',s) 
print(newtext) #will print the file without the expression, just plain text. 

#convert into individual words
words = newtext.split() 
print(words)

#convert all four letters words into words with asterisk

for wordi in range(len(words)):
	if len(words[wordi])==4:
		words[wordi] = words[wordi][0] + '***' #append first word of 4 letter word with ***

print(words) #will print all 4 letter words like this - h***, n*** etc.

#Put back together into one string
cleantext = ' '.join(words)
print(cleantext)

#this will create a new file names clean_transcipt.txt and write the clean text in it
with open('clean_transcript.txt','w') as f:
  f.write(cleantext)


#Scrambled the words

text = "I have often wondered whether it's possible to read an entire book faster if the useless letters were removed."
words = text.split()
print(words) #print the splited words in a list


for wi in range(len(words)):
	thisword = words[wi]
	idx = np.random.permutation(len(thisword))
	words[wi] = ''.join([thisword[i] for i in idx])

print(words)	#print the splited words in randomize e.g - ['I', 'eavh', 'efotn', 'odwdreen', 'etehrwh',.....,]

words = ' '.join(words)
print(words) #print the whole text in with randomize words e.g - I hvae etofn deronwed eerthwh...... 