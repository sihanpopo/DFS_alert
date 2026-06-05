import requests

url = "https://www.ssgdfs.com/kr/goos/initDetailGoos?goos_cd=100618000150"

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
print("notiReqBtn FOUND:", "notiReqBtn" in html)

print("\n===== HTML 시작 =====\n")
print(html[:2000])
print("\n===== HTML 끝 =====")
