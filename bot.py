import telebot
import requests
import json



TELEGRAM_TOKEN = '683089446:AAHwRWlhKSrwGCwMjBJU3pgyCdWBL9K1NZ0'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_chat_action(274660540, action = "typing")
    # tc = message.chat
    # telegram_user = "👤👤👤👤👤\nID: {0}\nFirst_name: {1}\nLast_name: {2}\nUsername: @{3}\nType: {4}".format(tc.id, tc.first_name, tc.last_name, tc.username, tc.type)
    # bot.send_message(274660540, telegram_user)

    bot.send_chat_action(message.chat.id, action = "typing")
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('🇬🇧 English', callback_data = 'English'))
    keyboard.add(telebot.types.InlineKeyboardButton('🇺🇦 Українська', callback_data = 'Ukrainian'))
    keyboard.add(telebot.types.InlineKeyboardButton('🇷🇺 Русский', callback_data = 'Russian'))
    bot.send_message(message.chat.id, 'Select your language: ', reply_markup = keyboard)

@bot.callback_query_handler(func=lambda x: True)
def callback_query(callback_query):
    message = callback_query.message
    text = callback_query.data
    if text == "English":
        bot.send_chat_action(message.chat.id, action = "typing")
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id, 'Perfectly! 🤖\n🔮 What can I do?\n        ✅ I can find the profile photo of any Instagram account in full size \n\n🔮 What is needed for this?\n        ✅ Just sent a username:\n                For example: @vova_peganov\n\n🔮 Something is not clear?\n        ✅ See the photo below 🖼')
        #bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text="тру-ту-ту")
        #bot.delete_message(chat_id, message_id=msg_id)
        #bot.send_message(message.chat.id, 'Добре!🙂\nЩоб я зміг надіслати тобі аватар Instagram - аккаунта у повному розмірі, ти маєш надіслати один варіант відповіді:\n    ✅ Ім’я користувача:\n        - Приклад: vova_peganov  або @vova_peganov\n    ✅ Посилання на профіль.\nПиши, я чекаю ⏱️💤')
    elif text == "Ukrainian":
        bot.send_chat_action(message.chat.id, action = "typing")
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id, 'Чудово! 🤖\n🔮 Що я вмію робити?\n        ✅ Я можу знаходити фото профілю будь-якого Інстаграм аккаунта у максимальній якості \n\n🔮 Що для цього потрібно?\n        ✅ Просто надішли ім’я користувача:\n                Наприклад: @vova_peganov\n\n🔮 Щось залишилося незрозумілим?\n        ✅ Дивись фото нижче 🖼')
    elif text == "Russian":
        bot.send_chat_action(message.chat.id, action = "typing")
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.send_message(message.chat.id, 'Замечательно! 🤖\n🔮 Что я умею делать?\n        ✅ Я могу находить фото профиля любого Инстаграм аккаунта в максимальном качестве \n\n🔮 Что для этого нужно?\n        ✅ Просто пришли имя пользователя:\n                Например: @vova_peganov\n\n🔮 Что-то осталось непонятным?\n        ✅ Смотри фото ниже 🖼')


@bot.message_handler(content_types=['text'])
def send_text(message):
    get_message = message.text
    inst_username = get_message.replace(' ', '').replace('@', '')
    if inst_username.lower() == 'vova_peganov':
        # bot.send_chat_action(274660540, action = "typing")
        # found_request = "🤐🤐🤐🤐🤐🤐🤐\nChat ID: {0}\nTG_Username: @{1}\nUsername: {2}\nStatus: SecretPhoto".format(str(message.chat.id), str(message.chat.username), str(inst_username))
        # bot.send_message(274660540, found_request)

        bot.send_chat_action(message.chat.id, action = "typing")
        bot.send_message(message.chat.id, 'Це фото засекречене! 🤫')
    else:
        user_information_request = requests.get('https://www.instagram.com/{0}/?__a=1'.format(inst_username))
        if user_information_request.status_code == 404: #203, 404, 502, 503
            # bot.send_chat_action(274660540, action = "typing")
            # found_request = "👎👎👎👎👎👎👎\nChat ID: {0}\nTG_Username: @{1}\nUsername: {2}\nStatus: NotFounded".format(str(message.chat.id), str(message.chat.username), str(inst_username))
            # bot.send_message(274660540, found_request)

            bot.send_chat_action(message.chat.id, action = "typing")
            bot.send_message(message.chat.id, 'Користувача не знайдено! Спробуй ще раз! 🔁')
            # if language == "English":
            #     bot.send_message(message.chat.id, 'User not found! Try again! 🔁')
            # elif language == "Ukrainian":
            #     bot.send_message(message.chat.id, 'Користувача не знайдено! Спробуйте ще раз! 🔁')
            # elif language == "Russian":
            #     bot.send_message(message.chat.id, 'Пользователя не найдено! Попробуйте еще раз! 🔁')
        elif user_information_request.status_code == 503:
            # bot.send_chat_action(274660540, action = "typing")
            # found_request = "❌❌❌❌❌❌❌\nChat ID: {0}\nTG_Username: @{1}\nUsername: {2}\nStatus: InstagramServerError".format(str(message.chat.id), str(message.chat.username), str(inst_username))
            # bot.send_message(274660540, found_request)

            bot.send_chat_action(message.chat.id, action = "typing")
            bot.send_message(message.chat.id, 'Неполадки на серверах Instagram 🤷‍\nСпробуй пізніше! 🔁')
        elif user_information_request.status_code == 200:
            # bot.send_chat_action(274660540, action = "typing")
            # found_request = "👍👍👍👍👍👍👍\nChat ID: {0}\nTG_Username: @{1}\nUsername: {2}\nStatus: Founded".format(str(message.chat.id), str(message.chat.username), str(inst_username))
            # bot.send_message(274660540, found_request)

            bot.send_chat_action(message.chat.id, action = "upload_photo")
            user_information_json = user_information_request.json()
            user_id = user_information_json['graphql']['user']['id']
            user_avatar = requests.get('https://i.instagram.com/api/v1/users/{0}/info/'.format(user_id)).json()
            user_avatar_url = user_avatar['user']['hd_profile_pic_url_info']['url']
            bot.send_photo(message.chat.id, photo=user_avatar_url)



#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')
#         bot.send_sticker(message.chat.id, 'CAADAgAD5gADtqs_Cx1MwwpmrYpVAg')
#         #bot.send_location(message.chat_id, '50.481654', '30.4855129')
#     else:
#         sitedata = requests.get("https://gramotool.ru/avatar/")
#         print(sitedata.content)
#
# @bot.message_handler(content_types=['sticker'])
# def send_text(message):
#     print(message)





bot.polling(none_stop=True, interval=0)
