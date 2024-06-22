import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    return requests.get(url)

def extract(page):
    soup = BeautifulSoup(page.text, "html.parser")
    return soup.select("article.Box-row")

def transform(html_repos):
    result = []
    for row in html_repos:
        repo_info = row.select_one("h2.h3.lh-condensed").text.strip().split('/')
        dev_name = repo_info[0].strip()
        repo_name = repo_info[1].strip()
        nbr_stars = row.select_one("a.Link--muted.d-inline-block.mr-3").text.strip().replace(',', '')
        result.append({
            "developer": dev_name,
            "repository_name": repo_name,
            "nbr_stars": nbr_stars
        })
    return result


def format(repositories_data):
    file = open("github_trends.csv", "w")
    file.write("Developer Name, Repository Name, Number of Stars\n")
    for row in repositories_data:
        file.write(f"{row['developer']}, {row['repository_name']}, {row['nbr_stars']}\n")
    file.close()
    print("Successfully created")


url = "https://github.com/trending"
response = request_github_trending(url)
extracted_data = extract(response)
transformed_data = transform(extracted_data)
format(transformed_data)

