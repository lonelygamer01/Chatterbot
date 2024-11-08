import requests

def get_google_news_regular(api_key, cx, total_news=40):
    all_news = []
    start = 1  # Start index for pagination, beginning with 1

    keywords = [
        "Szeged", "Szegeden", "Szegedi",
        "Budapest", "Magyarország", "Magyarországon",
        "politika", "oktatás", "egészség", "egészségügy",
        "informatika", "Orbán", "Magyar Péter", "Tisza párt",
        "Fidesz", "Kultúra", "járvány", "klímaváltozás",
        "gazdaság", "munka", "bűnözés", "sport",
        "művészet", "szórakozás", "tudomány", "ellenzék",
        "választások", "demonstráció", "jogok", "Pécs",
        "Debrecen", "Nyíregyháza", "Európai Unió", "NATO",
        "szegénység", "jövedelem", "szociális", "infláció",
        "foglalkoztatás", "kórház", "járványügyi", "oltás",
        "egészségügyi rendszer", "fesztivál", "színház",
        "irodalom", "zene", "tánc", "egyetem",
        "iskola", "tanulás", "diák", "ifjúság",
        "bíróság", "törvény", "kormány", "alkotmány",
        "állampolgárság", "természetvédelem", "környezetvédelem",
        "fenntarthatóság", "szennyezés", "digitális",
        "technológia", "innováció", "start-up", "közlekedés",
        "infrastruktúra", "autópálya", "vasút", "időjárás"
    ]
    query = " OR ".join(keywords) 

    while len(all_news) < total_news:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": api_key,
            "cx": cx,
            "q": query,
            "hl": "hu",
            "num": 10,
            "start": start
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get("items", [])
            for item in results:
                title = item["title"]
                link = item["link"]
                # Ensure uniqueness by checking for new titles only
                if title not in [news["title"] for news in all_news]:
                    all_news.append({"title": title, "link": link})
                # Stop if we’ve reached the desired count
                if len(all_news) >= total_news:
                    break
        else:
            print("Failed to fetch news")
            break
        # Increment start by 10 to get the next "page"
        start += 10

    return all_news

def get_google_news_szeged(api_key, cx, total_news=20):
    all_news = []
    start = 1  # Start index for pagination, beginning with 1

    keywords = [
        "Szeged", "Szegeden", "Szegedi"]
    query = " OR ".join(keywords) 

    while len(all_news) < total_news:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": api_key,
            "cx": cx,
            "q": query,
            "hl": "hu",
            "num": 10,
            "start": start
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get("items", [])
            for item in results:
                title = item["title"]
                link = item["link"]
                # Ensure uniqueness by checking for new titles only
                if title not in [news["title"] for news in all_news]:
                    all_news.append({"title": title, "link": link})
                # Stop if we’ve reached the desired count
                if len(all_news) >= total_news:
                    break
        else:
            print("Failed to fetch news")
            break
        # Increment start by 10 to get the next "page"
        start += 10

    return all_news

# Example usage
api_key = "AIzaSyABnsmdl8lUH7-OAZAqas6Be8dGncNErMo "
cx = "f20f59782833045e6"
google_news_regular = get_google_news_regular(api_key, cx)

google_news_szeged = get_google_news_szeged(api_key, cx)

for idx, item in enumerate(google_news_regular, 1):
    print(f"{idx}. {item['title']}")
    print(f"   Link: {item['link']}")

