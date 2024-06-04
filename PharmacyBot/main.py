import vk_api
import requests
from bs4 import BeautifulSoup
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='fe2036ad82af7507be908a270582ec155263e235c958932bf35e20103e3b8ea15384303a85d4e491af341')

def SendMsg(user_id, msg):
    vk_session.method("messages.send", {
        "user_id": user_id,
        "message": msg,
        "random_id": 0
    })

def SendMsgList(user_id, query):
    try:
        list = Find(query)
        text = ""
        for i in range(0, len(list[0])):
            text += "{0}.{1} - {2}р.\n".format(str(i+1), list[0][i], list[1][i])
        SendMsg(user_id, text)
    except:
        SendMsg(user_id, "К сожалению, ничего не найдено.")

def FindIn(page, query):
    block = page.findAll(class_=query)
    list = []
    for data in block:
        list.append(data.text)
    newlist = []
    for item in list:
        word = ""
        for l in item:
            if l == "\n" and word != "":
                break
            if not(l.isspace()) or word != "":
                word += l
        newlist.append(word)
    return newlist

def Find(text):
    url = 'https://farmakopeika.ru/search?query={}&availability=is_available_in_pharmacies&limit_=48&limit=48'.format(str(text))
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    fulllist = []
    fulllist.append(FindIn(soup,'product__title'))
    fulllist.append(FindIn(soup, 'product__price-text'))

    return fulllist

for event in VkLongPoll(vk_session).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        txt=event.text.lower()
        user_id=event.user_id

        if txt == "привет":
            SendMsg(user_id, "Здравствуйте!")
        elif txt != "":
            SendMsgList(user_id, txt)