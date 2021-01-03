import json

def parse_articles(raw_content):

    return raw_content["articles"]

def display_article(article):
    print(f"From {article["author"]}")



f = open("news.json", "w")
my_dict = json.(f)
# print(my_dict.keys())
# print(my_dict["articles"][0].keys())
f.close()
articles = parse_articles(my_dict)

# print(articles[0].keys())
print(articles[0]["title"])
for i in range(5):
    display_article(articles[i])
