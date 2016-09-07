# coding: UTF-8
import os
 
import sae
import web
import model
import dataProc
from weixinInterface import WeixinInterface
 
urls = (
'/', 'Hello',
'/recommendPosNeg', 'recommendPosNeg',
'/weixin','WeixinInterface',
'/ck','feedback',
)
 
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)
 
class Hello:
    def GET(self):
    #print "你好"
        return render.hello("你好")
    
class recommendPosNeg:
    def GET(self):
    #print "你好"
        poss,negs,generatedate=dataProc.readpos_neg()
        return render.recommendPosNeg(poss,negs,generatedate)
    
class feedback:
    def GET(self):
        fkcon = model.get_fkcontent()
        return render.checkfk(fkcon)
    
app = web.application(urls, globals()).wsgifunc()
        
application = sae.create_wsgi_app(app)
