import requests
import json
import sqlite3
import pandas as pd
import time

def main(page):
	url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1005&productId=1384071&score=0&sortType=6&page=%d&pageSize=10&isShadowSku=0&rid=0&fold=1' % page
	headers = {
		'Cookie': '__jdv=76161171|direct|-|none|-|1572504439541; __jdu=1572504439539291940601; areaId=2; shshshfpa=3c3ca02c-81d7-45c3-689a-0b01ed159404-1572504441; __jdc=122270672; shshshfp=2811d1b0a5a7044a50395693102ad41f; shshshfpb=ov72aSePpO9i4wfFL%20n26%2Fw%3D%3D; ipLoc-djd=2-2825-51931-0; 3AB9D23F7A4B3C9B=PLNK7PFMHN2X6JNHDBTPNZQJQCUOOVGBWZ6WMBFBHRDSLJPX6WMTTA7CAIA3HRZJXEVT4IZIAHIGIKPP4SM4HIHWXA; wlfstk_smdl=3btiv6aes0la6pxe52qo7jdald0g6f89; shshshsID=ac80c7f1a15dafffb102213f3a602f39_1_1572820272331; __jda=122270672.1572504439539291940601.1572504440.1572508113.1572820272.3; __jdb=122270672.1.1572504439539291940601|3.1572820272; JSESSIONID=D49DDB8F9127083520930D706E5DD957.s1',
		'Host': 'sclub.jd.com',
		'Referer': 'https://item.jd.com/1384071.html',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
	}
	s = requests.session()
	text = s.get(url=url, headers=headers).text
	comments = json.loads(text[text.find('(') + 1: -2]).get('comments')
	columns = ['content', 'creationTime', 'nickname', 'score']
	frame = pd.DataFrame(comments)[columns]

	def aux(ser):
		cursor = conn.cursor()
		cursor.execute('insert into jd_comments_api_comment (content, creationTime, nickname, score) values ("%s", "%s", "%s", %d)' % tuple(ser.values))
	frame.apply(aux, axis=1)

	print 'Page%d has completed.' % page

if __name__ == '__main__':
	conn = sqlite3.connect('jd_comment.db')
	cursor = conn.cursor()
	try:
		cursor.execute('create table jd_comments_api_comment (id integer primary key autoincrement, content varchar(100), creationTime timestamp, nickname varchar(20), score integer)')
	except OperationalError:
		pass

	for i in range(10):
		main(i)
		time.sleep(3)

	cursor.close()
	conn.commit()
	conn.close()

