import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt

# 1. 네이버 뉴스 IT/과학 기사 크롤링 (네이버 뉴스 IT/과학 랭킹뉴스 이용)
url = "https://news.naver.com/main/rank/sectionList.naver?sid1=105" # IT/과학(섹션 코드: 105)
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# 2. 뉴스 제목 추출
titles = []
for t in soup.select('.list_title'):
    titles.append(t.get_text())

print("수집된 뉴스 제목 개수:", len(titles))

# 3. 명사 추출로 워드클라우드 입력 만들기
okt = Okt()
words = []
for title in titles:
    words += okt.nouns(title)

# 4. 불용어(의미 없는 단어들) 제거 (간단히)
stopwords = set(['IT', '과학', '뉴스', '관련', '네이버', '속보', '경우', '오늘', '이슈', '기자'])
words_cleaned = [w for w in words if len(w) > 1 and w not in stopwords]

text = ' '.join(words_cleaned)

# 5. 워드클라우드 만들기
wc = WordCloud(font_path='malgun.ttf', background_color="white", width=800, height=400).generate(text)

plt.figure(figsize=(10,6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()