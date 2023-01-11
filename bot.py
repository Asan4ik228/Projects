import telebot
from datetime import datetime
from datetime import timedelta
from telebot import types
from random import randint

token = '5082755438:AAGhr6Xy_hHVafJmFDFJSiZ6KxWcXiMg4yQ'
bot = telebot.TeleBot(token)
myid = 987747961
t = datetime.now() + timedelta(hours=3)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Сегодня")
    item2 = types.KeyboardButton("Завтра")
    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Хей, {0.first_name}!\nЯ был ботом по рассылки расписания, но меня уволили, все из-за этого \
                     сранного сайта с расписаниями, видете ли он такой удобный, работает без перебоев, Асану было \
                     вообще наплевать, но я же не просто бот с расписанием...".format(
                         message.from_user),
                     parse_mode='html', reply_markup=markup)


users_name = ['Я', 'Юра', 'Витя', 'Наташа', 'Андрей', 'Вова', 'Саня', 'Кристина', 'Полина', 'Мурад', 'Женя', 'Рустем',
              'Серега']
users_id = [987747961, 1104366725, 1392399775, 1759968026, 541259320, 1289039138, 1781110107, 433731618, 1360741124,
            1360613411, 5134261433, 1971574147, 1437586611]
prepods = [['Широков', 'Игорь', 'Борисович'],
           ['Кудрявченко', 'Иван', 'Владимирович'],
           ['Макаров', 'Виктор', 'Константинович'],
           ['Деордица', 'Сергей', 'Витальевич'],
           ['Ломоносов', 'Сергей', 'Евгеньевич'],
           ['Мурзин', 'Дмитрий', 'Геннадьевич'],
           ['Еремина', 'Юлия', 'Юрьевна'],
           ['Зубенко', 'Наталья', 'Викторовна'],
           ['Корж', 'Елена', 'Николаевна']]
mats = ['хуй', "Хуй", 'Еблан', 'идорас', 'андон', 'Сука', 'ебок', 'ебище', 'ебал', 'Пидор', 'лять', "лядь", "еблан"]
namat = ['Сам', "токсик", "Кто как обзывается, тот сам так называется",
         'Не забывай, я имею доступ к данным твоего телефона)', "Мне же обидно 😖", "Ясно, бан",
         'Скажи это мне в жизни, интернет герой', 'Я вижу плохие слова в твоем сообщении']
noans = ['Не понял', 'Сори, не понял, Асану лень прописать мне ответы', 'Прости, что?',
         'Я хз что ответить', 'Ты расписание уже посмотрел?', 'ага, да, я все понял', 'че?', 'ладно',
         'Error, your phone reboot after 5 sec', 'Не может быть', 'Не верю', '?%%;(*%(*"3646 err', 'Ты это мне?',
         'Честно?', 'Скажи мне это в жизни, интернет герой', 'Чтобы это не значило, я за Путина', 'Хочешь анектод?',
         'Хм', '...', 'Помоги мне, Асан взял меня в плен и заставляет отвечать на ваши сообщения от лица бота',
         'Я устал вам отвечать', 'Это не входит в список моих команд']
ques = ['Нет наверное', 'Думаю да', 'Хз', 'Я че гУгЛ, вопросы мне задаешь)', 'угу', 'не уверен']
weekdays = ['онедельник', 'торник', 'реда', 'етверг', 'ятница', 'уббота', 'оскресенье']


def search(spis, mes):
    for i in spis:
        if i in mes:
            return True


def norasp(chatid):
    ans = ['Я больше не знаю расписание, Асан урезал мои возможности',
           'У меня больше нет данных о раписании, Асан дал предпочтение бездушному сайту...',
           'Прости, я больше не знаю расписание, мой функционал теперь ограничен',
           'Я не знаю что в этот день, Асан ограничел мне доступ, отдав приимущество дешевому сайту с расписанием...',
           'Я больше не знаю распиание...',
           'У меня больше нет расписания, мой функционал теперь ограничен...',
           'Я больше не могу рассылать расписание, Асан решил что дерьмосайт с расписанием лучше чем я',
           'Прости, у меня больше нет расписания']
    bot.send_message(chatid, ans[randint(0, len(ans)-1)])


def answer(mes, message):
    time = datetime.now() + timedelta(hours=3)
    r = randint(0, 2)
    for x in prepods:
        for y in range(3):
            if mes == x[y]:
                bot.send_message(message.chat.id, " ".join(x))
                return
    if search(mats, mes):
        if r == 0:
            pic = open(f'static/mat/{randint(0, 10)}.webp', 'rb')
            bot.send_sticker(message.chat.id, pic)
            return
        else:
            ans = namat[randint(0, len(namat) - 1)]
    elif 'Давай' in mes or 'давай' in mes:
        ans = "Жена давать будет)"
    elif mes == "шоколадно" or mes == "Шоколадно":
        ans = "Ээ, это моя фишка"
    elif mes == 'Ладно' or mes == 'ладно':
        ans = "Шоколадно)"
    elif mes == 'Да' or mes == 'да':
        ans = "Пизда)"
    elif mes == 'Нет' or mes == 'нет':
        ans = "Пидора ответ)"
    elif 'урак' in mes or 'ибил' in mes:
        ans = "Сам"
    elif 'ак тебя зовут' in mes or 'Кто ты' in mes:
        ans = "Я - гуль"
    elif 'атары' in mes or 'атарин' in mes:
        ans = 'ТАТАРЫ СИЛА'
    elif 'звини' in mes:
        vid = open('static/sorry.mp4', 'rb')
        bot.send_video(message.chat.id, vid)
        return
    elif mes == "Хочу" or mes == "хочу":
        ans = 'хоти'
    elif 'ривет' in mes or 'дарова' in mes or 'драствуй' in mes:
        ans = 'Привет'
    elif 'салам' in mes or 'Салам' in mes:
        ans = 'Алейкум, брат'
    elif 'е как' in mes or 'ак сам' in mes or 'ак дела' in mes:
        ans = 'Та норм, сам как?'
    elif 'делаешь' in mes:
        ans = 'Чай пью, что я еще могу делать'
    elif 'то делать' in mes:
        ans = 'Муравью хуй приделать'
    elif 'пасиб' in mes or 'лагодарю' in mes or 'агъ ол' in mes:
        ans = 'Обращайся)'
    elif mes == 'Дата':
        ans = f'Сервак: {datetime.now()} Русс: {time}'
    elif 'Пока' in mes or 'пока' in mes:
        ans = 'Пока, если что пиши)'
    elif '?' in mes:
        ans = ques[randint(0, len(ques) - 1)]
    else:
        for i in range(len(weekdays)):
            if weekdays[i] in mes:
                norasp(message.chat.id)
        if r == 0:
            pic = open(f'static/noans/{randint(0, 5)}.webp', 'rb')
            bot.send_sticker(message.chat.id, pic)
            return
        ans = noans[randint(0, len(noans) - 1)]
    bot.send_message(message.chat.id, ans)
    return


@bot.message_handler(content_types=['text'])
def group(message):
    if message.chat.type == 'private':
        if message.chat.id == myid:
            if message.text[:5] == "#all ":
                for i in users_id:
                    bot.send_message(i, message.text[5:])
                bot.send_message(myid, "Отправил всем")
                return
            elif message.text[0] == '!':
                id_name = message.text[1:message.text.find(" ")]
                text = message.text[message.text.find(' ') + 1:]
                for i in range(len(users_id)):
                    if users_name[i] == id_name:
                        bot.send_message(users_id[i], text)
                bot.send_message(myid, f"Отправил {id_name}")
                return
            elif message.text[:7] == "#video ":
                for i in users_id:
                    vid = open(f'static/{message.text[7:]}.mp4', 'rb')
                    bot.send_video(i, vid)
                bot.send_message(myid, "Отправил видео всем")
                return
        if 'егодня' in message.text or 'автра' in message.text:
            norasp(message.chat.id)
        else:
            answer(message.text, message)
    if message.chat.id != myid:
        bot.send_message(myid, f'{message.chat.first_name} пишет "{message.text}"')
        if message.chat.id not in users_id:
            bot.send_message(myid, f'Новый юзер {message.chat.first_name}, id {message.chat.id}')


def main():
    bot.polling(none_stop=True, interval=0, timeout=10)


if __name__ == '__main__':
    main()
