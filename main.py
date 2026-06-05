import requests

products = [
    {
        "site": "ssg",
        "name": "SPB317",
        "url": "https://www.ssgdfs.com/kr/goos/initDetailGoos?goos_cd=100618000150"
    },
    {
        "site": "ssg",
        "name": "SWR107",
        "url": "https://www.ssgdfs.com/kr/goos/initDetailGoos?goos_cd=100618000222"
    },
    {
        "site": "shilla",
        "name": "SPB317",
        "url": "https://www.shilladfs.com/estore/kr/ko/p/5768726"
    },
    {
        "site": "shilla",
        "name": "SWR107",
        "url": "https://www.shilladfs.com/estore/kr/ko/p/5746936"
    }
]

for product in products:

    html = requests.get(
        product["url"],
        headers={"User-Agent": "Mozilla/5.0"}
    ).text

    if product["site"] == "ssg":
        soldout = 'name="notiReqBtn"' in html

    elif product["site"] == "shilla":
        soldout = "requestRestockNotiBtn" in html

    if soldout:
        print(f"❌ 품절 - {product['name']}")
    else:
        print(f"✅ 재고 있음 - {product['name']}")
