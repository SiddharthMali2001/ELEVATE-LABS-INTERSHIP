import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raises error for 4xx/5xx

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for idx, h in enumerate(headlines, start=1):
            title = h.text.strip()
            if title:
                file.write(f"{idx}. {title}\n")

    print("✅ Headlines saved to headlines.txt")

except requests.exceptions.RequestException as e:
    print("❌ Error while fetching the website:", e)
except Exception as e:
    print("❌ An unexpected error occurred:", e)    