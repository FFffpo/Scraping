import pymysql
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='Wzf04132', db='mysql')
# charset='utf8' 读写中文

cur = conn.cursor()
cur.execute('USE scraping')
curselect = cur.execute('SELECT * FROM pages WHERE id =1')
print(cur.fetchone())

cur.close()
conn.close()
