

from googlesearch import search

# to search
query = "amazon"

for link in search(query=query, tld="com", num=10, stop=20, pause=4):
    print(link)