from pyrogram import Client, Filters
import time
api_id = "1208098"
api_hash = "31449da46f94afaaa6c632f3ca9a4c36"

print("first")
with Client("my_account", api_id, api_hash) as app:
    print("second")
    app.send_message("me", "Hi there! I'm using **Pyrogram**")

print("third")
# chat = 'https://t.me/joinchat/Sa8Y6h1o7rJVkPzfU3vFhQ' #Ссылка на чат
# userlist = ['@Xenoxbot','@vadyan_z'] #список юзеров, которых надо пригласить
# titleofchat = 'test' #тут будет переменная для названия чата
# themeofchat = 'какая-нибудь тема' #тема чата (общие интересы)
#timer = переменная для времени работы для чата, по истечению которого все будут удалены из него, как и сообщения

# app.create_group(title = titleofchat, users = userlist)
# mssg = app.send_message(chat_id, themeofchat)
# app.pin_chat_message(chat_id, mssg.message_id)

# Таймер беседы
#def kick_all_members(chat_id,users_id,timer):
    #time.sleep(timer)
    #ppl = app.get_chat_members_count(chat_id)
    #for i in ppl:
       #app.kick_chat_member(chat_id, users_id)
    #app.delete_message(message.chat.id, messagebd.message_id) удаление всех сообщений по id из бд
#kick_all_members(chat_id, users_id, timer = time)



app.run()