# -*- coding: utf-8 -*-
import sys
import ntchat
import handle_file

wechat = ntchat.WeChat()

# 打开pc微信, smart: 是否管理已经登录的微信
wechat.open(smart=True)


# 注册消息回调
@wechat.msg_register([ntchat.MT_RECV_IMAGE_MSG, ntchat.MT_RECV_PICTURE_MSG, ntchat.MT_RECV_VIDEO_MSG])
def on_recv_text_msg(wechat_instance: ntchat.WeChat, message):
    handle_file.do(message)


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
