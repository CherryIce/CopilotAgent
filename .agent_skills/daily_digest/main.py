# Daily AI Digest Skill
import requests
from datetime import date

def fetch_news():
    # 可替换成真实新闻API调用
    return [
        {'title': 'AI突破：超大模型训练新算法', 'url': 'https://example.com/ai-news1'},
        {'title': 'GitHub Copilot性能实测', 'url': 'https://example.com/ai-news2'}]

if __name__ == "__main__":
    news = fetch_news()
    fname = f".agent_memory/digests/{date.today()}.md"
    with open(fname, "w", encoding="utf-8") as f:
        print(f"# AI 日报\n", file=f)
        for item in news:
            print(f"- [{item['title']}]({item['url']})", file=f)
    print(f"AI 日报已写入: {fname}")
