import sys
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup

RSS_URL = "https://www.yna.co.kr/rss/news.xml"
LIMIT = 10
TIMEOUT = 10

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def clean_text(text: str) -> str:
    return " ".join(text.split()) if text else ""


def clean_summary(raw_html: str) -> str:
    if not raw_html:
        return "요약 없음"
    text = BeautifulSoup(raw_html, "html.parser").get_text(" ", strip=True)
    text = clean_text(text)
    return text if text else "요약 없음"


def get_text(item: ET.Element, tag: str, default: str) -> str:
    elem = item.find(tag)
    if elem is None or elem.text is None:
        return default
    value = elem.text.strip()
    return value if value else default


def fetch_article_content(url: str) -> str:
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        if not response.encoding:
            response.encoding = response.apparent_encoding
    except requests.RequestException:
        return "기사 본문을 가져오지 못했습니다."

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "noscript", "iframe", "header", "footer", "nav"]):
        tag.decompose()

    container = (
        soup.select_one(".story-news")
        or soup.select_one("#articleWrap")
        or soup.select_one("article")
    )

    candidates = container.find_all("p") if container else soup.find_all("p")

    paragraphs = []
    seen = set()
    for p in candidates:
        text = clean_text(p.get_text(" ", strip=True))
        if len(text) < 25:
            continue
        if "무단 전재" in text or "재배포 금지" in text:
            continue
        if "제보는 카카오톡" in text:
            continue
        if text in seen:
            continue
        seen.add(text)
        paragraphs.append(text)

    if not paragraphs:
        return "기사 본문을 추출하지 못했습니다."

    return "\n".join(paragraphs)


def fetch_rss(url: str, limit: int = 10):
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    items = root.findall("./channel/item")[:limit]

    results = []
    for item in items:
        title = get_text(item, "title", "제목 없음")
        summary_raw = get_text(item, "description", "")
        link = get_text(item, "link", "링크 없음")
        pub_time = get_text(item, "pubDate", "발행시간 없음")
        content = fetch_article_content(link)

        results.append(
            {
                "title": title,
                "summary": clean_summary(summary_raw),
                "link": link,
                "pub_time": pub_time,
                "content": content,
            }
        )

    return results


def print_news(news_list):
    if not news_list:
        print("가져온 뉴스가 없습니다.")
        return

    print(f"총 {len(news_list)}건\n")
    for i, news in enumerate(news_list, 1):
        print(f"[{i}] {news['title']}")
        print(f"  - 요약: {news['summary']}")
        print(f"  - 링크: {news['link']}")
        print(f"  - 발행: {news['pub_time']}")
        print("  - 기사내용:")
        print(news["content"])
        print("-" * 100)


if __name__ == "__main__":
    try:
        news_items = fetch_rss(RSS_URL, LIMIT)
        print_news(news_items)
    except requests.RequestException as e:
        print(f"RSS 요청 실패: {e}")
    except ET.ParseError as e:
        print(f"RSS 파싱 실패: {e}")
