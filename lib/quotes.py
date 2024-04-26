import requests

def Fetch():
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data['content']
        author = data['author']
        print(f"Quote: {quote}")
        print(f"Author: {author}")
    else:
        print("Failed to retrieve random quote.")