import pymysql
sql='/*--user=root;--password=123456;--host=192.168.1.5;--execute=1;--port=3306;--enable-ignore-warnings=1;--split=1*/\
inception_magic_start;\
use mysql;\
CREATE TABLE adaptive_office2(id int);\
create table adaptive_office3(id int);\
insert into adaptive_office2(10);\
insert into adaptive_office3(10);\
inception_magic_commit;'
try:
    conn=pymysql.connect(host='192.168.1.6', user='', passwd='', db='', port=6669)
    cur=conn.cursor()
    ret=cur.execute(sql)
    result=cur.fetchall()
    # num_fields = len(cur.description)
    # field_names = [i[0] for i in cur.description]
    print(result)
    # for row in result:
    #     print(row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",
    #     row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10])
    cur.close()
    conn.close()
except Exception as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))