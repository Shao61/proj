import sqlite3

conn = sqlite3.connect('db.sqlite')

c = conn.cursor()

# c.execute('''
#     CREATE TABLE comments (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     updated_at DATETIME,
#     video_id INTEGER,
#     user_id INTEGER,
#     content TEXT,
#     FOREIGN KEY (video_id) REFERENCES videos(id),
#     FOREIGN KEY (user_id) REFERENCES users(id)
#     );
# ''')




# c.execute("INSERT INTO videos (title, decsription, url, cover) VALUES (?, ?, ?, ?)", ('','說明 APCS 觀念題不同題型的解題思路步驟，追蹤指令的執行過程例如迴圈、遞迴函式、條件判斷等常見題型','','')
c.execute("update videos set cover = 'https://i.ytimg.com/vi/AqU3LtcpPaA/hqdefault.jpg' where id = '8'")
conn.commit()

conn.close()