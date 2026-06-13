# Web Crawling Practice

BeautifulSoup과 Selenium을 활용한 웹 크롤링 실습 레포지토리입니다.

## 학습 목적
핀인사이트 인턴십 사전 준비로 온라인 뉴스 데이터 수집 역량을 키우기 위해 학습했습니다.

## 기술 스택
- Python 3.x
- BeautifulSoup4
- Selenium
- requests

## 실습 목록
| 파일 | 설명 |
|------|------|
| bbc_crawl.py | BBC News 기사 제목·링크·날짜·카테고리 수집 후 CSV 저장 |

## 학습 내용
- BeautifulSoup으로 정적 페이지 크롤링
- find / find_all / find_parent 메서드 활용
- data-testid 속성으로 태그 탐색
- 수집 데이터 CSV 저장

## 실행 방법
```bash
pip3 install requests beautifulsoup4
python3 bbc_crawl.py
```