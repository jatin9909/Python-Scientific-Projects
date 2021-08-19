import re
import string
import numpy as np

pattern2replace = '\\n\\n\d{1,3}\\n\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\\n'
with open("subtitle.txt","r",encoding="utf8") as rfile:
	s=rfile.read()

regex_timestamps = re.compile('%s'%pattern2replace)
regex_timestamps.findall(s)

newtext = regex_timestamps.sub(' ',s)
print(newtext)

with open('clean_transcript.txt','w',encoding="utf8") as f:
  f.write(newtext)