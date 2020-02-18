import urllib.request
import pandas as pd
title = []
date = []
url = []
author = []
p = 0
while p != 20:
    p = p + 1
    cate = 'cutting-edge/ai/page/'+'%d'%p
    page = urllib.request.urlopen("https://technews.tw/category/%s/"%cate)
    text = page.read().decode("utf8")
    titleurlFind = text.split("bookmark\">")
    authorFind = text.split("author\">")
    dateFind = text.split("發布日期</span>")
    n = 0
    for line in dateFind[1:]:
        n = n + 1
        splittitle = titleurlFind[n].index("</a>")
        splitdate = dateFind[n].index("</span>")
        splitauth = authorFind[n].index("</a>")
        spliturl1 = titleurlFind[n-1].index("class=\"entry-title\"><a href=\"")
        spliturl2 = titleurlFind[n-1].index("\" title=\"")
        title.append(titleurlFind[n][:splittitle])
        date.append(dateFind[n][28:splitdate])
        author.append(authorFind[n][:splitauth])
        url.append(titleurlFind[n-1][spliturl1+29:titleurlFind[n-1].find(title[n-1])-9])
group = ["Title", "Author", "Date", "Link"]
AI_dict = {
        "Title":title,
        "Author":author,
        "Date":date,
        "Link":url
        }
AI_df = pd.DataFrame(AI_dict)
