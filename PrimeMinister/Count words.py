import wikipedia
# s = wikipedia.summary("Wikipedia")
# # Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...
# print(s)
# #wikipedia.search("Barack")
# # [u'Barak (given name)', u'Barack Obama', u'Barack (brandy)', u'Presidency of Barack Obama', u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, 2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']

# ny = wikipedia.page("New York")
# # ny.title
# # # u'New York'
# # ny.url
# # # u'http://en.wikipedia.org/wiki/New_York'
# print(ny.content)
# u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
#ny.links[0]
# u'1790 United States Census'
result = wikipedia.search("2021 in the United States")
print(result)
page = wikipedia.page(result[0],auto_suggest=False)
content = page.content
print(content)
res = len(content.split())
print(res)

# import matplotlib.pyplot as plt
# y=['A.P.J Abdul Kalam','Atal Bihari Vajpayee', 'K.R. Narayanan', 'Narendra Modi', 'Indira Gandhi', 'Jawaharlal nehru']
  
# # getting values against each value of y
# x=[6110,6859,6941,10664,12790,13683] 
# plt.barh(y, x)
  
# # setting label of y-axis
# plt.ylabel("pen sold")
  
# # setting label of x-axis
# plt.xlabel("price") 
# plt.title("Horizontal bar graph")
# plt.show()