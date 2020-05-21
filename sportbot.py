import telebot
import conf
from telebot import types
from collections import defaultdict
bot=telebot.TeleBot(conf.TOKEN)
clients={}
baskets={}
menu = types.KeyboardButton('Вернуться в меню')
class goods:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(True,True)
        swim = types.KeyboardButton('Плавание')
        run = types.KeyboardButton('Бег')
        combat = types.KeyboardButton('Единоборства')
        tennis = types.KeyboardButton('Теннис')
        football = types.KeyboardButton('Футбол')
        basketball = types.KeyboardButton('Баскетбол')
        self.markup.row(swim, run, combat)
        self.markup.row(football, basketball, tennis)
        self.markup.row(menu)
class product:
    def __init__(self,name,price,image):
        self.name = name
        self.price = price
        self.image = image
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class swim(goods):
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(True,True)
        plavki = types.KeyboardButton('Плавки')
        kupalnik = types.KeyboardButton('Купальник')
        shapochka = types.KeyboardButton('Шапочки')
        ochki = types.KeyboardButton('Очки')
        polotence = types.KeyboardButton('Полотенца')
        self.markup.row(plavki, kupalnik)
        self.markup.row(shapochka, ochki, polotence)
        self.markup.row(menu)
cross1 = open('pictures/cross1.jpg','rb')
cross2 = open('pictures/cross2.jpg','rb')
cross3 = open('pictures/cross3.jpg','rb')
cross4 = open('pictures/cross4.jpg','rb')

goods_all = goods()
swim = swim()

plavki1 = product('Спортивные плавки',500,open('pictures/plavki1.jpg','rb'))
plavki2 = product('Спортивные плавки шорты',600,open('pictures/plavki2.jpg','rb'))
plavki3 = product('Плавки как шорты',300,open('pictures/plavki3.jpg','rb'))
kupalnik1 = product('Купальник обычный',300,open('pictures/kupalnik1.jpg','rb'))
kupalnik2 = product('Купальник спортивный',8000,open('pictures/kupalnik2.jpg','rb'))
shapochka1 = product('Шапочка женская',300,open('pictures/shapochka1.jpg','rb'))
shapochka2 = product('Шапочка мужская',300,open('pictures/shapochka2.jpg','rb'))
ochki1 = product('Очки простые',100,open('pictures/ochki1.jpg','rb'))
ochki2 = product('Очки супер крутые',5000,open('pictures/ochki2.jpg','rb'))
polotence1 = product('Полотенце быстросохнущее',5000,open('pictures/polotence1.jpg','rb'))
polotence1 = product('Полотенце быстросохнущее',5000,open('pictures/polotence2.jpg','rb'))
goods = ['plavki1','plavki2','plavki3','kupalnik1','kupalnik2','shapochka1','shapochka2','ochki1','ochki2','polotence1','polotence2']


all = types.ReplyKeyboardMarkup(True,True)

info = types.KeyboardButton('Заполнить информацию о себе')
order = types.KeyboardButton('Оформить заказ')
range = types.KeyboardButton('Посмотреть ассортимент')
basket1 = types.KeyboardButton('Проверить корзину')
all.row(info)
all.row(range)
all.row(basket1)
all.row(order)
all.row(menu)
menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_markup.add(menu)
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

start_p,name_p,sername_p,telephone_p,adress_p,confirmation = 1,2,3,4,5,6

user_state = defaultdict(lambda:start_p)
user_id = ''
user_first_name = ''
user_last_name = ''
user_telephone = ''
user_adress = ''
def get_state(message):
    return user_state[message.chat.id]
def update_state(message, state):
    user_state[message.chat.id] = state
@bot.message_handler(commands=['start'])
def welc(message):
    global user_id
    global user_first_name
    global user_last_name
    global baskets
    user_id = message.chat.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    baskets.update({user_id:[]})
    bot.send_message(message.chat.id, "Здравствуйте! Вы попали в магазин 'всё для спорта'")
    bot.send_message(message.chat.id, "Что вы хотите сделать?", reply_markup=all)
@bot.message_handler(func=lambda message:get_state(message) == start_p)
def range(message):
    if message.text == 'Посмотреть ассортимент':
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=goods_all.markup)
    elif message.text == 'Плавание':
        bot.send_message(message.chat.id, "Какие плавательные принадлежности вам нужны?", reply_markup=swim.markup)
    elif message.text == 'Плавки':
        bot.send_message(message.chat.id, "Выбирайте",reply_markup=menu_markup)
        bot.send_photo(message.chat.id, plavki1.image, plavki1.name + ' ' + str(plavki1.price) + 'р', reply_markup=plavki1.markup)
        bot.send_photo(message.chat.id, plavki2.image, plavki2.name + ' ' + str(plavki2.price) + 'р',reply_markup=plavki2.markup)
        bot.send_photo(message.chat.id, plavki3.image, plavki3.name + " " + str(plavki3.price) + 'р',reply_markup=plavki3.markup)
    elif message.text == 'Купальник':
        bot.send_message(message.chat.id, "Выбирайте",reply_markup=menu_markup)
        bot.send_photo(message.chat.id, kupalnik1.image, kupalnik1.name + " " + str(kupalnik1.price) + 'р',reply_markup=kupalnik1.markup)
        bot.send_photo(message.chat.id, kupalnik2.image, kupalnik2.name + " " + str(kupalnik1.price) + 'р',reply_markup=kupalnik2.markup)
    elif message.text == 'Шапочки':
        bot.send_message(message.chat.id, "Выбирайте",reply_markup=menu_markup)
        bot.send_photo(message.chat.id, shapochka1.image, shapochka1.name + " " + str(kupalnik1.price) + 'р',reply_markup=shapochka1.markup)
        bot.send_photo(message.chat.id, shapochka2.image, shapochka2.name + " " + str(kupalnik2.price) + 'р',reply_markup=shapochka2.markup)
    elif message.text == 'Очки':
        bot.send_message(message.chat.id, "Выбирайте",reply_markup=menu_markup)
        bot.send_photo(message.chat.id, ochki1.image, ochki1.name + " " + str(ochki1.price) + 'р',reply_markup=ochki1.markup)
        bot.send_photo(message.chat.id, ochki2.image, ochki2.name + " " + str(ochki1.price) + 'р',reply_markup=ochki2.markup)
    elif message.text == 'Полотенца':
        bot.send_message(message.chat.id, "Выбирайте",reply_markup=menu_markup)
        bot.send_photo(message.chat.id, polotence1.image, polotence1.name + " " + str(polotence1.price) + 'р',reply_markup=polotence1.markup)
        bot.send_photo(message.chat.id, polotence2.image, polotence2.name + " " + str(polotence1.price) + 'р',reply_markup=polotence2.markup)
    elif message.text == 'Бег':
        bot.send_message(message.chat.id, "Какие кроссовки вам нужны?", reply_markup=runs)
    elif message.text == 'Женские':
        bot.send_message(message.chat.id, "Выбирайте",reply_markup=menu_markup)
        cross1s = types.InlineKeyboardMarkup(row_width=1)
        cross1b = types.InlineKeyboardButton("добавить в корзину", callback_data='Женские кроссовки беговые')
        cross1s.add(cross1b)
        bot.send_photo(message.chat.id, cross1, "Женские кроссовки беговые 5000р",reply_markup=cross1s)
        cross2s = types.InlineKeyboardMarkup(row_width=1)
        cross2b = types.InlineKeyboardButton("добавить в корзину", callback_data='Женские кроссовки для прогулки')
        cross2s.add(cross2b)
        bot.send_photo(message.chat.id, cross2, "Женские кроссовки для прогулки 2000р",reply_markup=cross2s)
    elif message.text == 'Мужские':
        bot.send_message(message.chat.id, "Выбирайте",reply_markup=menu_markup)
        cross3s = types.InlineKeyboardMarkup(row_width=1)
        cross3b = types.InlineKeyboardButton("добавить в корзину", callback_data='Мужские кроссовки беговые')
        cross3s.add(cross3b)
        bot.send_photo(message.chat.id, cross3, "Мужские кроссовки беговые 5000р",reply_markup=cross3s)
        cross4s = types.InlineKeyboardMarkup(row_width=1)
        cross4b = types.InlineKeyboardButton("добавить в корзину", callback_data='Мужские кроссовки для прогулки')
        cross4s.add(cross4b)
        bot.send_photo(message.chat.id, cross4, "Мужские кроссовки для прогулки 2000р",reply_markup=cross4s)
    elif message.text == 'Единоборства':
        bot.send_message(message.chat.id, "Какой вид единоборств вам нужен?", reply_markup=combats)
    elif message.text == 'Теннис':
        bot.send_message(message.chat.id, "Настольный или большой?", reply_markup=tenisses)
    elif message.text == 'Футбол':
        bot.send_message(message.chat.id, "Что именно вам надо?", reply_markup=footballs)
    elif message.text == 'Баскетбол':
        bot.send_message(message.chat.id, "Что именно вам надо?", reply_markup=basketballs)
    elif message.text == 'Проверить корзину':
        pass
    elif message.text == 'Заполнить информацию о себе':
        name = types.InlineKeyboardMarkup(row_width=2)
        yes = types.InlineKeyboardButton("да", callback_data='name_yes')
        no = types.InlineKeyboardButton("нет", callback_data='name_no')
        name.row(yes,no)
        #name.row(menu)
        bot.send_message(message.chat.id, "Ваc зовут " + user_first_name + ' ' + user_last_name + '?', reply_markup=name)
@bot.message_handler(func=lambda message:get_state(message) == name_p)
def name_request(message):
    global user_first_name
    user_first_name = message.text
    bot.send_message(message.chat.id,'Напишите вашу фамилию')
    update_state(message, sername_p)
@bot.message_handler(func=lambda message:get_state(message) == sername_p)
def last_name_request(message):
    global user_last_name
    user_last_name = message.text
    telephone_markup = types.ReplyKeyboardMarkup(True,True)
    telephone_button = types.KeyboardButton('Отправить свой номер', request_contact=True)
    telephone_markup.row(telephone_button)
    bot.send_message(message.chat.id,'Напишите номер телефона или отправьте с помощью кнопки', reply_markup=telephone_markup)
    update_state(message,telephone_p)
@bot.message_handler(func=lambda message:get_state(message) == telephone_p)
@bot.message_handler(content_types=["contact"])
def telephone_request(message):
    global user_telephone
    user_telephone = message.contact.phone_number
    bot.send_message(message.chat.id,'Напишите свой адрес')
    update_state(message,adress_p)
@bot.message_handler(func=lambda message:get_state(message) == adress_p)
def adress_request(message):
    global user_adress
    user_adress = message.text
    confirm = types.InlineKeyboardMarkup(row_width=2).add(types.KeyboardButton('да'),types.KeyboardButton('нет'))
    bot.send_message(message.chat.id,'Все правильно?' + '\n' + user_first_name + ' ' + user_last_name + '\n' + user_telephone + '\n' + user_adress,reply_markup=confirm)
    update_state(message,confirmation)
@bot.message_handler(func=lambda message:get_state(message) == confirmation)
def confirm_request(message):
    if message.text == 'да':
        update_state(message,start_p)
        clients.update({user_id:{'user_first_name':user_first_name,'user_last_name':user_last_name,'user_telephone':user_telephone,'user_adress':user_adress,'chat_id':message.chat.id}})
@bot.message_handler(content_types=['text'])
def order(message):
    print('fddf')
    bot.send_message(message.chat.id,'blabla')
    if message.text == 'Оформить заказ':
        print('dvvdvvdvvdv')
        bot.send_message(message.chat.id,'ura nakonec to')
        for x in baskets:
            if x == message.chat.id:
                bot.send_message(message.chat.id,'Ваши данные' + '\n' + user_first_name + ' ' + user_last_name + '\n' + user_telephone + '\n' + user_adress)
                bot.send_message(message.chat.id,'Ваш заказ')
                for x in baskets[x]:
                    bot.send_message(message.chat.id,x)
        confirm1 = types.InlineKeyboardMarkup(True,True).add(types.InlineKeyboardButton(text='да',callback_data='confirm_yes'),types.InlineKeyboardButton(text='нет',callback_data='confirm_no'))
        bot.send_message(message.chat.id,'Все верно?',reply_markup=confirm1)

@bot.callback_query_handler(func=lambda call:True)
def buy(call):
    try:
        if call.message:
            if call.data == 'name_no':
                bot.send_message(call.message.chat.id,'Напишите ваше имя')
                update_state(call.message, name_p)
            elif call.data == 'name_yes':
                telephone_markup = types.ReplyKeyboardMarkup(True,True)
                telephone_button = types.KeyboardButton('Отправить свой номер', request_contact=True)
                telephone_markup.row(telephone_button)
                bot.send_message(call.message.chat.id,'Напишите номер телефона или отправьте с помощью кнопки', reply_markup=telephone_markup)
                update_state(call.message,telephone_p)
            elif call.data == 'confirm_yes':
                bot.send_message(call.message.chat.id,'Ваш заказ отправлен')
                for x in clients:
                    if call.message.chat.id == x:
                        for y in baskets:
                            if call.message.chat.id == y:
                                bot.send_message(conf.admin_chat_id,clients[x]+'\n'+baskets[y])
            else:
                bot.send_message(call.message.chat.id, call.data + ' добавлено в корзину')
                baskets[call.message.chat.id].append(call.data)
    except Exception as e:
        print(e)

bot.polling(none_stop=True)
