import json

def article_to_html(article):
    '''
    Convert into article_to_html
    '''
    html_code = """
        <div class = "news-block">
          <p class="new-author">Author:{article['author']}</p>
          <p class = "new-content">Content:article['title']}</p>
          <small class = "news-date">Published:article['publishedAt']}</small>
        </div>
    """
def display_article(article):
    print(f"From {article['author']}: {article['title']}")
full_html_code = """
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link rel="style.css" href="/css/master.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <title></title>
  </head>
  <body>
"""
f = open("news.json", "r")
content = json.load(f)
f.close()
for article in articles:
    html_article = article_to_html(article)
    full_html_code += html_code
# article_0_in_html = article_to_html(articles[0])
# print(article_0_in_html)
"""
html_code += """
  </body>
</html>
"""
f = open("index.html", "w")
f.write(full_html_code)
f.close()
print("Finished!")
# articles = parse_articles(content)

# for i in range(5):
#     display_article(articles[i])
print(article[0])
