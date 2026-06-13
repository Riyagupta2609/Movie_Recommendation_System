import requests

API_KEY = "7374f3da35a66d8ce0eb0adf51693984"

url = f"https://api.themoviedb.org/3/movie/155?api_key={API_KEY}"

response = requests.get(
    url,
    headers={"User-Agent":"Mozilla/5.0"}
)

print(response.status_code)
print(response.json()["title"])