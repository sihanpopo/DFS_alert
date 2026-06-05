import requests

url = "https://www.shilladfs.com/estore/kr/ko/p/5768726"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

html = response.text

print("HTTP STATUS:", response.status_code)
print("HTML LENGTH:", len(html))
print("requestRestockNotiBtn FOUND:", "requestRestockNotiBtn" in html)
print(html[:1000])
