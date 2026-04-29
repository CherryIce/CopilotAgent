import sys, requests
from bs4 import BeautifulSoup

def seo_audit(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    title = soup.title.string if soup.title else ""
    h1 = [h.get_text() for h in soup.find_all("h1")]
    return f"# SEO报告\nURL: {url}\n\nTitle: {title}\nH1: {h1}"

if __name__ == "__main__":
    url = sys.argv[1]
    print(seo_audit(url))
