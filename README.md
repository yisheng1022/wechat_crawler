# wechat_crawler
## wechat_func.py
1. to_html()可將txt檔轉成html檔，方便後續解析
2. wechat_catch()可將上述得到的html檔解析成以下資料
    </br>◆ 文章網址(url)
    </br>◆ 文章標題(title)
    </br>◆ 文章發布日期(date)
    </br>◆ 文章作者(author) ※目前僅顯示原創文章
    </br>◆ 文章全文(content)
    </br>◆ 文章多媒體數量(media)
    </br>◆ 文章發布帳號(account)
3. 最終檔案將存成csv檔

### to_html(filename)
    ◆ 此function目前只提供html to txt
    ◆ 目前只有一個參數需要輸入
### wechat_catch(filename)
    ◆ 此function只能解析wechat的文章頁面
    ◆ 目前只有一個參數需要輸入
    ◆ 範例頁面：https://reurl.cc/lR1yGq (完整網址：https://mp.weixin.qq.com/s?__biz=MzU2MjkxODg3MA==&mid=2247558024&idx=3&sn=f8ecb29669220a51f85a43df8f9c34bc&chksm=fc618731cb160e27a25f07a9f56b1b7fd3011dad2d9e41226ecabb5b2e002cc2c3f1f87e5c05&scene=38#wechat_redirect)
