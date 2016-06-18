# coding: UTF-8
import os
 
import sae
import web
import model
 
from weixinInterface import WeixinInterface
 
urls = (
'/', 'Hello',
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
    
class feedback:
    def GET(self):
        fkcon = model.get_fkcontent()
        return render.checkfk(fkcon)
    
app = web.application(urls, globals()).wsgifunc()
        
application = sae.create_wsgi_app(app)
