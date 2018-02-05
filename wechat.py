import itchat
import pymysql


def get_conn():
    db_conn = pymysql.connect(
        host="localhost",
        db="wechat",
        user="root",
        passwd="123456",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return db_conn


def close_conn(db_conn):
    db_conn.close()


def get_friends():
    itchat.login()
    return itchat.get_friends(update=True)


def insert_db():
    friends = get_friends()

    for friend in friends:
        db_conn = get_conn()
        if friend['NickName'] == 'joshua':
            continue
        sql = "insert into t_wechat_friends (sex, nickname, signature, province, city)" + \
              " values(" + str(friend['Sex']) + ",'" + friend['NickName'] + "','" + friend['Signature'] + "','" + \
              friend['Province'] + "','" + friend['City'] + "');"
        print(sql)
        with db_conn.cursor() as cursor:
            cursor.execute(sql)
            db_conn.commit()
            close_conn(db_conn)


if __name__ == '__main__':
    insert_db()
