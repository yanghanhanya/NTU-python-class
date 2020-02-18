from pyquery import PyQuery as pq
from lxml import etree

def main():
  doc = pq('https://technews.tw/category/cutting-edge/ai/')
  titles = doc("h1")
  for title in titles.items():
    print(title.text())

if __name__=="__main__":
  main()