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

# 转换支持中文
# ALTER DATABASE wiki_threads CHARACTER SET=utf8mb4 COLLATE utf8mb4_unicode_ci;
# ALTER TABLE pages CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
# ALTER TABLE pages CHANGE title title VARCHAR(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# TRUNCATE TABLE pages;清空数据表
