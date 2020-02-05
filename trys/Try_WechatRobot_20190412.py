import requests
import itchat #这是一个用于微信回复的库
KEY = '92f9e5997161430682bf7ef9b28af2df' #这个key可以直接拿来用
 
# 向api发送请求
def get_response(msg):
  Url = 'http://www.tuling123.com/openapi/api'
  data = {
    'key'  : KEY,
    'info'  : msg,
    'userid' : 'pth-robot',
  }
  try:
    r = requests.post(Url, data=data).json()
    return r.get('text')
  except:
    return
 
# 注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
  # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
  defaultReply = '不想理你了'
  # 如果图灵Key出现问题，那么reply将会是None
  reply = get_response(msg['Text'])
  # a or b的意思是，如果a有内容，那么返回a，否则返回b
  return reply or defaultReply
 
#开启群聊是isGroupChat=True，默认为false#'isAt'是微信的@符号
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        defaultReply='机器人故障中...'
         # 如果图灵Key出现问题，那么reply将会是None
        reply = get_response(msg['Text'])
         # a or b的意思是，如果a有内容，那么返回a，否则返回b
        if reply==None:
            reply=defaultReply
        reply="@%s\u2005"%(msg['ActualNickName'])+reply
        return reply
def reply_msg(msg):
    print("收到一条信息：",msg.text)
# 为了让修改程序不用多次扫码,使用热启动
itchat.auto_login(hotReload=True)
itchat.run()
