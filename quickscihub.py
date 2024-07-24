import requests
import sys
from bs4 import BeautifulSoup
import json
import os

query = sys.argv[1].strip()
timeout_seconds = int(os.environ["timeout"])

domains = ["https://sci-hub.st/", "https://sci-hub.ru/", "https://sci-hub.se/"]

def check_page_exists(url, domain, timeout=timeout_seconds):
    try:
        response = requests.head(url, timeout=timeout)
        if response.status_code == 200:  # 200 means the page exists
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string

            if "article not found" not in title:
                # get download link
                buttons_div = soup.find("div", id="buttons")
                button = buttons_div.find("button")
                onclick_value = button.get("onclick")
                start_index = onclick_value.find("'") + 1
                end_index = onclick_value.rfind("'")
                partial_url = onclick_value[start_index:end_index]
                if partial_url.startswith(r"//"):
                    download_url = f"https:{partial_url}"
                elif partial_url.startswith(r"/downloads"):
                    download_url = f"{domain}{partial_url}"

                return title, download_url
        return "Sci-Hub: article not found", None
    except requests.exceptions.RequestException as e:
        return "Sci-Hub: article not found", None

def extract_doi_suffix(link):
    # Check if "doi.org/" is present in the link
    if "doi.org/" in link:
        # Find the index of "doi.org/" and extract the substring after it
        return link.split("doi.org/")[-1]
    return link

identifier = extract_doi_suffix(query)

page_url = f"{domains[0]}{identifier}"

title, download_url = check_page_exists(page_url, domains[0])
if title.endswith("article not found"):
    responses = [check_page_exists(f"{dm}{identifier}", dm) for dm in domains[1:]]
    if all("article not found" in r[0] for r in responses):
        result = title
    else:
        for i, r in enumerate(responses):
            if "article not found" not in r[0]:
                title = r[0].split("|")[1].split(".")[0]
                result = f"{r[1]}||{title}"
else:
    title = title.split("|")[1].split(".")[0]
    result = f"{download_url}||{title}"

sys.stdout.write(result)

