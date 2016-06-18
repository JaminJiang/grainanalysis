# _*_ coding:utf-8 _*_
import web
import web.db
import sae.const


db = web.database(
    dbn='mysql',
    host=sae.const.MYSQL_HOST,
    port=int(sae.const.MYSQL_PORT),
    user=sae.const.MYSQL_USER,
    passwd=sae.const.MYSQL_PASS,
    db=sae.const.MYSQL_DB
)
 
def addfk(username, fktime, fkcontent):
    return db.insert('fk', user=username, time=fktime, fk_content=fkcontent)
 
def get_fkcontent():
    return db.select('fk', order='id')
