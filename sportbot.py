import telebot
import conf
from telebot import types
bot=telebot.TeleBot(conf.TOKEN)

plavki1 = open('C:/Users/gusev/telbot/pictures/plavki1.jpg','rb')
plavki2 = open('C:/Users/gusev/telbot/pictures/plavki2.jpg','rb')
plavki3 = open('C:/Users/gusev/telbot/pictures/plavki3.jpg','rb')
kupalnik1 = open('C:/Users/gusev/telbot/pictures/kupalnik1.jpg','rb')
kupalnik2 = open('C:/Users/gusev/telbot/pictures/kupalnik2.jpg','rb')
shapochka1 = open('C:/Users/gusev/telbot/pictures/shapochka1.jpg','rb')
shapochka2 = open('C:/Users/gusev/telbot/pictures/shapochka2.jpg','rb')
ochki1 = open('C:/Users/gusev/telbot/pictures/ochki1.jpg','rb')
ochki2 = open('C:/Users/gusev/telbot/pictures/ochki2.jpg','rb')
polotence1 = open('C:/Users/gusev/telbot/pictures/polotence1.jpg','rb')
polotence2 = open('C:/Users/gusev/telbot/pictures/polotence2.jpg','rb')

basket = []

all = types.ReplyKeyboardMarkup(True,True)
order = types.KeyboardButton('Сделать заказ')
range = types.KeyboardButton('Посмотреть ассортимент')
basket1 = types.KeyboardButton('Проверить корзину')
all.row(order)
all.row(range)
all.row(basket1)

goods = types.ReplyKeyboardMarkup(True,True)
swim = types.KeyboardButton('Плавание')
run = types.KeyboardButton('Бег')
combat = types.KeyboardButton('Единоборства')
tennis = types.KeyboardButton('Теннис')
football = types.KeyboardButton('Футбол')
basketball = types.KeyboardButton('Баскетбол')
goods.row(swim, run, combat)
goods.row(football, basketball, tennis)

swims = types.ReplyKeyboardMarkup(True,True)
plavki = types.KeyboardButton('Плавки')
kupalnik = types.KeyboardButton('Купальник')
shapochka = types.KeyboardButton('Шапочки')
ochki = types.KeyboardButton('Очки')
polotence = types.KeyboardButton('Полотенца')
swims.row(plavki, kupalnik)
swims.row(shapochka, ochki, polotence)

runs = types.ReplyKeyboardMarkup(True,True)
zhcross = types.KeyboardButton('Женские кроссовки')
mcross = types.KeyboardButton('Мужские кроссовки')
runs.row(zhcross, mcross)

combats = types.ReplyKeyboardMarkup(True,True)
box = types.KeyboardButton('Бокс')
sambo = types.KeyboardButton('Самбо')
karate = types.KeyboardButton('Каратэ')
combats.row(box, sambo, karate)

tennises = types.ReplyKeyboardMarkup(True,True)
table = types.KeyboardButton('Настольный')
plain = types.KeyboardButton('Большой')
tennises.row(table, plain)

footballs = types.ReplyKeyboardMarkup(True,True)
fballs = types.KeyboardButton('Мячи')
fboots = types.KeyboardButton('Кроссовки')
other = types.KeyboardButton('Другое')
footballs.row(box, sambo, karate)

basketballs = types.ReplyKeyboardMarkup(True,True)
bballs = types.KeyboardButton('Мячи')
bboots = types.KeyboardButton('Кроссовки')
bother = types.KeyboardButton('Одежда')
basketballs.row(bballs, bboots, bother)
@bot.message_handler(commands=['start'])
def welc(message):
    bot.send_message(message.chat.id, "Здравствуйте! Вы попали в магазин 'всё для спорта'")
    bot.send_message(message.chat.id, "Что вы хотите сделать?", reply_markup=all)
@bot.message_handler(content_types=['text'])
def range(message):
    if message.text == 'Посмотреть ассортимент':
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=goods)
    elif message.text == 'Плавание':
        bot.send_message(message.chat.id, "Какие плавательные принадлежности вам нужны?", reply_markup=swims)
    elif message.text == 'Плавки':
        bot.send_message(message.chat.id, "Выбирайте")
        plavki1s = types.InlineKeyboardMarkup(row_width=1)
        plavki1b = types.InlineKeyboardButton("добавить в корзину", callback_data='plavki 1')
        plavki1s.add(plavki1b)
        bot.send_photo(message.chat.id, plavki1, "Спортивные плавки 500р",reply_markup=plavki1s)
        plavki2s = types.InlineKeyboardMarkup(row_width=1)
        plavki2b = types.InlineKeyboardButton("добавить в корзину", callback_data='plavki 2')
        plavki2s.add(plavki2b)
        bot.send_photo(message.chat.id, plavki2, "Спортивные плавки шорты 600р",reply_markup=plavki2s)
        plavki3s = types.InlineKeyboardMarkup(row_width=1)
        plavki3b = types.InlineKeyboardButton("добавить в корзину", callback_data='plavki 3')
        plavki3s.add(plavki3b)
        bot.send_photo(message.chat.id, plavki3, "Плавки как шорты 300р",reply_markup=plavki3s)
    elif message.text == 'Купальник':
        bot.send_message(message.chat.id, "Выбирайте")
        kupalnik1s = types.InlineKeyboardMarkup(row_width=1)
        kupalnik1b = types.InlineKeyboardButton("добавить в корзину", callback_data='kupalnik 1')
        kupalnik1s.add(kupalnik1b)
        bot.send_photo(message.chat.id, kupalnik1, "Купальник обычный 300р",reply_markup=kupalnik1s)
        kupalnik2s = types.InlineKeyboardMarkup(row_width=1)
        kupalnik2b = types.InlineKeyboardButton("добавить в корзину", callback_data='kupalnik 2')
        kupalnik2s.add(kupalnik2b)
        bot.send_photo(message.chat.id, kupalnik2, "Купальник спортивный 700р",reply_markup=kupalnik2s)
    elif message.text == 'Шапочки':
        bot.send_message(message.chat.id, "Выбирайте")
        shapochka1s = types.InlineKeyboardMarkup(row_width=1)
        shapochka1b = types.InlineKeyboardButton("добавить в корзину", callback_data='shapochka 1')
        shapochka1s.add(shapochka1b)
        bot.send_photo(message.chat.id, shapochka1, "Шапочка женская 300р",reply_markup=shapochka1s)
        shapochka2s = types.InlineKeyboardMarkup(row_width=1)
        shapochka2b = types.InlineKeyboardButton("добавить в корзину", callback_data='shapochka 2')
        shapochka2s.add(shapochka2b)
        bot.send_photo(message.chat.id, shapochka2, "Шапочка мужская 300р",reply_markup=shapochka2s)
    elif message.text == 'Очки':
        bot.send_message(message.chat.id, "Выбирайте")
        ochki1s = types.InlineKeyboardMarkup(row_width=1)
        ochki1b = types.InlineKeyboardButton("добавить в корзину", callback_data='ochki 1')
        ochki1s.add(ochki1b)
        bot.send_photo(message.chat.id, ochki1, "Очки простые 100р",reply_markup=ochki1s)
        ochki2s = types.InlineKeyboardMarkup(row_width=1)
        ochki2b = types.InlineKeyboardButton("добавить в корзину", callback_data='ochki 2')
        ochki2s.add(ochki2b)
        bot.send_photo(message.chat.id, ochki2, "Очки супер крутые 5000р",reply_markup=ochki2s)
    elif message.text == 'Полотенца':
        bot.send_message(message.chat.id, "Выбирайте")
        polotence1s = types.InlineKeyboardMarkup(row_width=1)
        polotence1b = types.InlineKeyboardButton("добавить в корзину", callback_data='polotence 1')
        polotence1s.add(polotence1b)
        bot.send_photo(message.chat.id, polotence1, "Полотенце быстросохнущее 500р",reply_markup=polotence1s)
        polotence2s = types.InlineKeyboardMarkup(row_width=1)
        polotence2b = types.InlineKeyboardButton("добавить в корзину", callback_data='polotence 2')
        polotence2s.add(polotence2b)
        bot.send_photo(message.chat.id, polotence2, "Полотенце пляжное 200р",reply_markup=polotence2s)
    elif message.text == 'Бег':
        bot.send_message(message.chat.id, "Какие кроссовки вам нужны?", reply_markup=runs)
    elif message.text == 'Единоборства':
        bot.send_message(message.chat.id, "Какой вид единоборств вам нужен?", reply_markup=combats)
    elif message.text == 'Теннис':
        bot.send_message(message.chat.id, "Настольный или большой?", reply_markup=tenisses)
    elif message.text == 'Футбол':
        bot.send_message(message.chat.id, "Что именно вам надо?", reply_markup=footballs)
    elif message.text == 'Баскетбол':
        bot.send_message(message.chat.id, "Что именно вам надо?", reply_markup=basketballs)

@bot.callback_query_handler(func=lambda call:True)
def buy(call):
    try:
        if call.message:
            if call.data == 'plavki 1':
                bot.send_message(call.message.chat.id, 'Спортивные плавки добавлены в корзину')
                basket.append(call.data)
            elif call.data == 'plavki 2':
                bot.send_message(call.message.chat.id,'Спортивные плавки шорты добавлены в корзину')
                basket.append(call.data)
            elif call.data == 'plavki 3':
                bot.send_message(call.message.chat.id,'Плавки как шорты добавлены в корзину')
                basket.append(call.data)
            elif call.data == 'kupalnik 1':
                bot.send_message(call.message.chat.id,'Купальник обычный добавлен в корзину')
                basket.append(call.data)
            elif call.data == 'kupalnik 2':
                bot.send_message(call.message.chat.id,'Купальник спортивный добавлен в корзину')
                basket.append(call.data)
            elif call.data == 'shapochka 1':
                bot.send_message(call.message.chat.id,'Шапочка женская добавлена в корзину')
                basket.append(call.data)
            elif call.data == 'shapochka 2':
                bot.send_message(call.message.chat.id,'Шапочка мужская добавлена в корзину')
                basket.append(call.data)
            elif call.data == 'ochki 1':
                bot.send_message(call.message.chat.id,'Очки простые добавлены в корзину')
                basket.append(call.data)
            elif call.data == 'ochki 2':
                bot.send_message(call.message.chat.id,'Очки супер крутые добавлены в корзину')
            elif call.data == 'polotence 1':
                bot.send_message(call.message.chat.id,'Полотенце быстросохнущее добавлено в корзину')
            elif call.data == 'polotence 2':
                bot.send_message(call.message.chat.id,'Полотенце пляжное добавлено в корзину')
    except Exception as e:
        print(e)

bot.polling(none_stop=True)
