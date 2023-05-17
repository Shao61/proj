import sqlite3

conn = sqlite3.connect('db.sqlite', check_same_thread=False)
cursor = conn.cursor()

def check_email(ch_email):
    e = cursor.execute(f"SELECT * FROM 'users' where email='{ch_email}'").fetchone()
    print('check_email', e)
    if  e is None:
        return True
    else:
        return False

def check_name(name):
    n = cursor.execute(f"SELECT * FROM 'users' where name='{name}'").fetchone()
    print('check_name', n)
    if n is None:
        return True
    else:
        return False

def check_login(email, pwd):
    p = cursor.execute(f"SELECT * FROM 'users' where email='{email}' and password = '{pwd}'").fetchone()
    print('check_account', p)
    if p is None:
        return False
    else:
        return True
    
def get_user(email):
    u = cursor.execute(f"SELECT * FROM 'users' where email='{email}'").fetchone()
    return u[1]

def get_videos():
    videos = cursor.execute(f"SELECT * FROM 'videos'").fetchall()
    return videos

def get_video(id):
    video = cursor.execute(f"SELECT * FROM 'videos' where id = '{id}'").fetchone()
    return video