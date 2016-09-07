# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import urllib2,json
from lxml import etree
import model

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def POST(self):        
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        mstype=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        if mstype == "event":
            mscontent = xml.find("Event").text
            if mscontent == "subscribe":
                replayText = u'''欢迎关注本微信，这个微信是本人业余爱好所建立，也是想一边学习Python一边玩的东西,现在还没有什么功能，只是弄了个翻译与豆瓣图书查询的小工具，你们有什么好的文章也欢迎反馈给我,我会不定期的分享给大家，输入help查看操作指令'''
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
            if mscontent == "unsubscribe":
                replayText = u'我现在功能还很简单，知道满足不了您的需求，但是我会慢慢改进，欢迎您以后再来'
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
        if mstype == 'text':
            content=xml.find("Content").text
            if content == 'help':
                replayText = u'''1.输入中文或者英文返回原文本.\n2.输入fk_反馈内容进行反馈，/ck下查看.'''
                return self.render.reply_text(fromUser,toUser,int(time.time()),replayText)
            elif content.startswith('fk'):
                fktime = time.strftime('%Y-%m-%d %H:%M',time.localtime())        
                model.addfk(fromUser,fktime,content[3:].encode('utf-8'))        
                return self.render.reply_text(fromUser,toUser,int(time.time()),u'感谢您的反馈')
            else :
                return self.render.reply_text(fromUser,toUser,int(time.time()),'echo: '+content)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="grainanalysis" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法        

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
