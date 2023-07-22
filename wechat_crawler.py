# from selenium import webdriver
import requests
from bs4 import BeautifulSoup as BS
from tqdm import tqdm, trange
import csv,os
import time
import random
import datetime,gc,builtins,threading
import pandas as pd
# import uuid

def to_html(filename):
	file_name = filename # str(file_count)+'_'+ date + '.txt'
	f = open(file_name,'r',encoding = 'utf-8')
	cont = f.read()
	htf_name = filename.replace('.txt','.html')
	htf = open(htf_name,'w',encoding = 'utf-8')
	htf.write(cont)
	f.close()
	htf.close()

def wechat_catch(filename,Date = '0818'):
	lock = threading.Lock()
	lock.acquire()	
	# for file_count in range(1,55):
	# 	file_name = str(file_count) + '_' + Date + '.html'
	file_name = filename
	if os.path.isfile(file_name):
		art_info = pd.DataFrame()
		f = open(file_name,'r',encoding = 'utf-8')
		all_page = BS(f.read(),'html.parser')
		f.close()
		# del file_name
		# gc.collect()
		media = all_page.select('strong#nickname')
		news_title = all_page.select('h4.weui_media_title')
		title_l = []
		for things in news_title:
			title_l.append(things.text)
		date = all_page.select('div.weui_media_bd.js_media p.weui_media_extra_info')
		date_l = []
		for day in date:
			date_l.append(day.text.replace("原创",""))
		arturl_l = []
		# print(news_title)
		for url in news_title:
			try:
				arturl_l.append(url['hrefs'])
			except:
				arturl_l.append('No url')
		progress = tqdm(total = len(arturl_l))
		art_info["url"] = arturl_l
		art_info["title"] = title_l
		art_info["date"] = date_l
		content_l = []
		media_count_l = []
		media_l = []
		author_l = []
		for link in arturl_l:
			progress.update(1)
			media_l.append(media[0].text)
			if link != 'No url':
				page_content = requests.get(link)
				page_content.encoding = 'utf-8'
				page_source = BS(page_content.text,'html.parser')
				tmp_content = page_source.select('div#js_content section span')
				autt = page_source.select('head meta')
				if len(autt) >= 22:
					for ggg in autt:
						try:
							if ggg['name'] == 'author':
								if ggg['content'] != "":
									author_l.append(ggg['content'].replace('&nbsp;','').replace(u'\u200b','').replace(u'\xa0',' '))
								else:
									author_l.append("原創")
						except:
							pass;
				else:
					author_l.append(" ")
				# print(author_l)
				if len(tmp_content) == 0:
					content_l.append(" ")
				else:
					cont_words = ""
					for content in tmp_content:
						cont_words = cont_words + content.text + "\n"
					content_l.append(cont_words)
				news_pic = page_source.select('div.rich_media_wrp img')
				news_video = page_source.select('txpdiv.txp_poster')
				news_sound = page_source.select('mpvoice')
				media_count_l.append(len(news_pic) + len(news_sound) + len(news_video))
				time.sleep(random.randint(3,7))
			else:
				content_l.append(" ")
				media_count_l.append(" ")
				author_l.append(" ")
			page_content.close()
			
		art_info["author"] = author_l
		art_info["content"] = content_l
		art_info["media"] = media_count_l
		art_info["account"] = media_l
		if os.path.isfile('wechat_crawlaa' + Date + '.csv'):
			art_info.to_csv('wechat_crawl' + Date + '.csv',mode = 'a+',header = False, index = False,encoding = 'utf-8')
			del media_l,content_l,media_count_l
			gc.collect()
		else:
			art_info.to_csv('wechat_crawl' + Date + '.csv',mode = 'a+',header = True, index = False,encoding = 'utf-8')
			del media_l,content_l,media_count_l
			gc.collect()



# wechat_catch('26_0904.html','0904')


