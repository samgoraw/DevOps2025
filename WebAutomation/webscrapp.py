from bs4 import BeautifulSoup

html = """
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p class="description">This is a test Page</p>
    <a href="https://sample.com">Visit Sample</a>
</body>
</html>
"""

#pass the html
soup = BeautifulSoup(html,'html.parser')

#get the title
print("title:",soup.title.text)

#get the heading
print("Heading:",soup.h1.text)
#extract the pargaraph with class attribute
print("Paragraph:",soup.find("p",class_="description").text)
#extract the url
print("Links:",soup.a["href"])