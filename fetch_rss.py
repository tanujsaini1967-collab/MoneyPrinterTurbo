import feedparser

# Aaj Tak ka RSS Feed Link (Bina API wala)
RSS_URL = "https://www.aajtak.in/rssfeed/?id=home"

def get_trending_horror_topic():
    try:
        feed = feedparser.parse(RSS_URL)
        if feed.entries:
            latest_title = feed.entries[0].title
            with open("topics.txt", "w", encoding="utf-8") as f:
                f.write(latest_title)
            print(f"Naya topic set ho gaya: {latest_title}")
        else:
            print("RSS feed se koi topic nahi mila!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_trending_horror_topic()

