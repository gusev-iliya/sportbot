import telebot
import conf
from telebot import types
from collections import defaultdict
bot=telebot.TeleBot(conf.TOKEN)
clients={}
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
class plavki(swim):
    pass
class plavki1(plavki):
    def __init__(self):
        self.image = open('pictures/plavki1.jpg','rb')
        self.name = 'Спортивные плавки'
        self.price = 500
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class plavki2(plavki):
    def __init__(self):
        self.image = open('pictures/plavki2.jpg','rb')
        self.name = 'Спортивные плавки шорты'
        self.price = 600
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class plavki3(plavki):
    def __init__(self):
        self.image = open('pictures/plavki3.jpg','rb')
        self.name = 'Плавки как шорты'
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class kupalnik(swim):
    pass
class kupalnik1(kupalnik):
    def __init__(self):
        self.image = open('pictures/kupalnik1.jpg','rb')
        self.name = 'Купальник обычный '
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class kupalnik2(kupalnik):
    def __init__(self):
        self.image = open('pictures/kupalnik2.jpg','rb')
        self.name = 'Купальник спортивный'
        self.price = 8000
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class shapochka(swim):
    pass
class shapochka1(shapochka):
    def __init__(self):
        self.image = open('pictures/shapochka1.jpg','rb')
        self.name = 'Шапочка женская'
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class shapochka2(shapochka):
    def __init__(self):
        self.image = open('pictures/shapochka2.jpg','rb')
        self.name = 'Шапочка мужская'
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class ochki(swim):
    pass
class ochki1(ochki):
    def __init__(self):
        self.image = open('pictures/ochki1.jpg','rb')
        self.name = 'Очки простые'
        self.price = 100
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class ochki2(ochki):
    def __init__(self):
        self.image = open('pictures/ochki2.jpg','rb')
        self.name = 'Очки супер крутые'
        self.price = 5000
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class polotence(swim):
    pass
class polotence1(polotence):
    def __init__(self):
        self.image = open('pictures/polotence1.jpg','rb')
        self.name = 'Полотенце быстросохнущее'
        self.price = 5000
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class polotence2(polotence):
    def __init__(self):
        self.image = open('pictures/polotence2.jpg','rb')
        self.name = 'Полотенце пляжное'
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class cross(goods):
    pass
class cross1(polotence):
    def __init__(self):
        self.image = open('pictures/polotence2.jpg','rb')
        self.name = 'Полотенце пляжное'
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class cross2(polotence):
    def __init__(self):
        self.image = open('pictures/polotence2.jpg','rb')
        self.name = 'Полотенце пляжное'
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class cross3(polotence):
    def __init__(self):
        self.image = open('pictures/polotence2.jpg','rb')
        self.name = 'Полотенце пляжное'
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
class cross4(polotence):
    def __init__(self):
        self.image = open('pictures/polotence2.jpg','rb')
        self.name = 'Полотенце пляжное'
        self.price = 300
        self.markup = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("добавить в корзину", callback_data=self.name)
        self.markup.add(button)
cross1 = open('pictures/cross1.jpg','rb')
cross2 = open('pictures/cross2.jpg','rb')
cross3 = open('pictures/cross3.jpg','rb')
cross4 = open('pictures/cross4.jpg','rb')

goods = goods()
swim = swim()
plavki1 = plavki1()
plavki2 = plavki2()
plavki3 = plavki3()
kupalnik1 = kupalnik1()
kupalnik2 = kupalnik2()
shapochka1 = shapochka1()
shapochka2 = shapochka2()
ochki1 = ochki1()
ochki2 = ochki2()
polotence1 = polotence1()
polotence2 = polotence2()

all = types.ReplyKeyboardMarkup(True,True)
order = types.KeyboardButton('Оформить заказ')
range = types.KeyboardButton('Посмотреть ассортимент')
basket1 = types.KeyboardButton('Проверить корзину')
all.row(order)
all.row(range)
all.row(basket1)

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

start_p,name_p,sername_p,telephone_p,adress_p,confirmation,confirmation1 = 1,2,3,4,5,6,7

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
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    bot.send_message(message.chat.id, "Здравствуйте! Вы попали в магазин 'всё для спорта'")
    bot.send_message(message.chat.id, "Что вы хотите сделать?", reply_markup=all)
@bot.message_handler(func=lambda message:get_state(message) == start_p)
def range(message):
    if message.text == 'Посмотреть ассортимент':
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup=goods.markup)
    elif message.text == 'Плавание':
        bot.send_message(message.chat.id, "Какие плавательные принадлежности вам нужны?", reply_markup=swim.markup)
    elif message.text == 'Плавки':
        bot.send_message(message.chat.id, "Выбирайте")
        bot.send_photo(message.chat.id, plavki1.image, plavki1.name + ' ' + str(plavki1.price) + 'р', reply_markup=plavki1.markup)
        bot.send_photo(message.chat.id, plavki2.image, plavki2.name + ' ' + str(plavki2.price) + 'р',reply_markup=plavki2.markup)
        bot.send_photo(message.chat.id, plavki3.image, plavki3.name + " " + str(plavki3.price) + 'р',reply_markup=plavki3.markup)
    elif message.text == 'Купальник':
        bot.send_message(message.chat.id, "Выбирайте")
        bot.send_photo(message.chat.id, kupalnik1.image, kupalnik1.name + " " + str(kupalnik1.price) + 'р',reply_markup=kupalnik1.markup)
        bot.send_photo(message.chat.id, kupalnik2.image, kupalnik2.name + " " + str(kupalnik1.price) + 'р',reply_markup=kupalnik2.markup)
    elif message.text == 'Шапочки':
        bot.send_message(message.chat.id, "Выбирайте")
        bot.send_photo(message.chat.id, shapochka1.image, shapochka1.name + " " + str(kupalnik1.price) + 'р',reply_markup=shapochka1.markup)
        bot.send_photo(message.chat.id, shapochka2.image, shapochka2.name + " " + str(kupalnik2.price) + 'р',reply_markup=shapochka2.markup)
    elif message.text == 'Очки':
        bot.send_message(message.chat.id, "Выбирайте")
        bot.send_photo(message.chat.id, ochki1.image, ochki1.name + " " + str(ochki1.price) + 'р',reply_markup=ochki1.markup)
        bot.send_photo(message.chat.id, ochki2.image, ochki2.name + " " + str(ochki1.price) + 'р',reply_markup=ochki2.markup)
    elif message.text == 'Полотенца':
        bot.send_message(message.chat.id, "Выбирайте")
        bot.send_photo(message.chat.id, polotence1.image, polotence1.name + " " + str(polotence1.price) + 'р',reply_markup=polotence1.markup)
        bot.send_photo(message.chat.id, polotence2.image, polotence2.name + " " + str(polotence1.price) + 'р',reply_markup=polotence2.markup)
    elif message.text == 'Бег':
        bot.send_message(message.chat.id, "Какие кроссовки вам нужны?", reply_markup=runs)
    elif message.text == 'Женские':
        bot.send_message(message.chat.id, "Выбирайте")
        cross1s = types.InlineKeyboardMarkup(row_width=1)
        cross1b = types.InlineKeyboardButton("добавить в корзину", callback_data='Женские кроссовки беговые')
        cross1s.add(cross1b)
        bot.send_photo(message.chat.id, cross1, "Женские кроссовки беговые 5000р",reply_markup=cross1s)
        cross2s = types.InlineKeyboardMarkup(row_width=1)
        cross2b = types.InlineKeyboardButton("добавить в корзину", callback_data='Женские кроссовки для прогулки')
        cross2s.add(cross2b)
        bot.send_photo(message.chat.id, cross2, "Женские кроссовки для прогулки 2000р",reply_markup=cross2s)
    elif message.text == 'Мужские':
        bot.send_message(message.chat.id, "Выбирайте")
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
    elif message.text == 'Оформить заказ':
        name = types.InlineKeyboardMarkup(row_width=2)
        yes = types.InlineKeyboardButton("да", callback_data='name_yes')
        no = types.InlineKeyboardButton("нет", callback_data='name_no')
        name.row(yes,no)
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
            clients.update({user_id:{'user_first_name':user_first_name,'user_last_name':user_last_name,'user_telephone':user_telephone,'user_adress':user_adress}})
        print(clients)
@bot.callback_query_handler(func=lambda call:True)
def buy(call):
    try:
        if call.message:
            if call.data == 'name_no':
                bot.send_message(call.message.chat.id,'Напишите ваше имя')
                update_state(call.message, name_p)
            elif call.data == 'name_yes':
                bot.send_message(call.message.chat.id,'Напишите номер телефона или отправьте с помощью кнопки', reply_markup=telephone_markup)
                update_state(call.message,telephone_p)
            else: bot.send_message(call.message.chat.id, call.data + 'добавлено в корзину')
            # if call.data == 'plavki 1':
            #     bot.send_message(call.message.chat.id, 'Спортивные плавки добавлены в корзину')
            #     basket.append(call.data)
            # elif call.data == 'plavki 2':
            #     bot.send_message(call.message.chat.id,'Спортивные плавки шорты добавлены в корзину')
            #     basket.append(call.data)
            # elif call.data == 'plavki 3':
            #     bot.send_message(call.message.chat.id,'Плавки как шорты добавлены в корзину')
            #     basket.append(call.data)
            # elif call.data == 'kupalnik 1':
            #     bot.send_message(call.message.chat.id,'Купальник обычный добавлен в корзину')
            #     basket.append(call.data)
            # elif call.data == 'kupalnik 2':
            #     bot.send_message(call.message.chat.id,'Купальник спортивный добавлен в корзину')
            #     basket.append(call.data)
            # elif call.data == 'shapochka 1':
            #     bot.send_message(call.message.chat.id,'Шапочка женская добавлена в корзину')
            #     basket.append(call.data)
            # elif call.data == 'shapochka 2':
            #     bot.send_message(call.message.chat.id,'Шапочка мужская добавлена в корзину')
            #     basket.append(call.data)
            # elif call.data == 'ochki 1':
            #     bot.send_message(call.message.chat.id,'Очки простые добавлены в корзину')
            #     basket.append(call.data)
            # elif call.data == 'ochki 2':
            #     bot.send_message(call.message.chat.id,'Очки супер крутые добавлены в корзину')
            #     basket.append(call.data)
            # elif call.data == 'polotence 1':
            #     bot.send_message(call.message.chat.id,'Полотенце быстросохнущее добавлено в корзину')
            #     basket.append(call.data)
            # elif call.data == 'polotence 2':
            #     bot.send_message(call.message.chat.id,'Полотенце пляжное добавлено в корзину')
            #     basket.append(call.data)
            # elif call.data == 'cross 1':
            #     bot.send_message(call.message.chat.id,'Женские кроссовки беговые добавлены в корзину')
            #     basket.append(call.data)
            # elif call.data == 'cross 2':
            #     bot.send_message(call.message.chat.id,'Женские кроссовки для прогулки добавлены в корзину')
            #     basket.append(call.data)
            # elif call.data == 'cross 3':
            #     bot.send_message(call.message.chat.id,'Мужские кроссовки беговые добавлены в корзину')
            #     basket.append(call.data)
            # elif call.data == 'cross 4':
            #     bot.send_message(call.message.chat.id,'Мужские кроссовки для прогулки добавлены в корзину')
            #     basket.append(call.data)
    except Exception as e:
        print(e)

bot.polling(none_stop=True)
