import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=URL)
website_as_html = response.text
# print(content)
soup = BeautifulSoup(website_as_html, "html.parser")
movies_order = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies_order.reverse()
# or reverse order using slice [::-1]
with open("movies.txt", "w", encoding="utf-8") as movie_ranked:
    for movie in movies_order:
        movie_ranked.write(f"{movie}\n")


