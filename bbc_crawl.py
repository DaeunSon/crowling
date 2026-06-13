import requests
from bs4 import BeautifulSoup
import csv

# BBC News 메인 페이지 요쳥
url = "https://www.bbc.com/news"

#일반 브라우저 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

#HTML 전체 받아오기
response = requests.get(url, headers=headers)
result = []

#beautifulsoup으로 파싱
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h2")

for i, title in enumerate(titles[:10]):
    #제목
    text = title.get_text(strip=True)
    parent_a = title.find_parent("a")
    if text and parent_a:
        #링크
        href = "https://www.bbc.com" + parent_a.get("href", "")
        #날짜
        date__tag = parent_a.find("span", {"data-testid": "card-metadata-lastupdated"})
        date = date__tag.get_text(strip=True) if date__tag else "날짜 없음"
        #카테고리
        category_tag = parent_a.find("span", {"data-testid": "card-metadata-tag"})
        category = category_tag.get_text(strip=True) if category_tag else "카테고리 없음"

        result.append({
            "제목": text,
            "링크": href,
            "날짜": date,
            "카테고리": category
        })

        print(f"{i+1}. {text}")
        print(f" 링크: {href}")
        print(f" 날짜: {date}")
        print(f" 카테고리: {category}")
        print()

#csv 저장
with open("bbc_news.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["제목", "링크", "날짜", "카테고리"])
    writer.writeheader()
    writer.writerows(result)

print("BBC 뉴스 크롤링 완료")
