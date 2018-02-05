import itchat


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['FromUserName'])
    print(msg.user)
    if msg.user.NickName == '文龙':
        msg.user.send('[Smile]')


itchat.auto_login()
itchat.run()


if __name__ == '__main__':
    print_content()
