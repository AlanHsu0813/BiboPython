import urllib.request as req
import bs4
import json

# 忽略 SSL 憑證驗證
# ssl._create_default_https_context = ssl._create_unverified_context

# Define the URL to fetch data from
url = "https://tabelog.com/tw/aichi/A2301/A230101/23075728/"

# Set up the request headers to mimic a browser request
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
})

with req.urlopen(request) as item_response:
    item_data = item_response.read().decode("utf-8")

root = bs4.BeautifulSoup(item_data, "html.parser")

name_wrap = root.find("div", class_="rstinfo-table__name-wrap")
num_wrap = root.find_all("strong", class_="rstinfo-table__tel-num")
cost_wrap = root.find_all("span", class_="rstinfo-table__budget-item")
# print(name_wrap)
# ######################### chatGTP
if name_wrap:
    restaurant_name = name_wrap.text.strip()  # 去除多餘的空白
    print("Restaurant Name:", restaurant_name)  # 輸出: Meieki Sushi Sublime

if num_wrap: # list
    # restaurant_num = num_wrap.text.strip()
    # print(num_wrap)
    for number in num_wrap:
        restaurant_num = number.text.strip()
        print("Restaurant num:", restaurant_num)

#if cost_wrap:
 #   for budget in cost_wrap:
  #      restaurant_cost = budget.text.strip()
   #     print("Restaurant cost:", restaurant_cost)

if cost_wrap:
    # 假設夜間價格是第一個元素，日間價格是第二個元素
    night_cost = cost_wrap[0].text.strip()
    day_cost = cost_wrap[1].text.strip()
    
    # 打印夜間與日間價格
    if night_cost:
        print("Nighttime price:", night_cost)
    if day_cost:
        print("Daytime price:", day_cost)