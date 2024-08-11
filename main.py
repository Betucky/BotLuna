import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply
from configparser import *

#Conexion con nuestro BOT

TOKEN = '7099130706:AAF978Cs1-pS30Iv-yKg8SMkvvweoCNd08o'

bot = telebot.TeleBot(TOKEN)
usuario= {}

#Creacion de comandos simples como `/start` y `/help`
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, 'Hola que tal, un gusto en saludarte, Somos LUNAS, nuestro objetivo es brindarte un espacio seguro para mujeres, donde puedas ser escuchada sin ser juzgada, asi que puedes experaste libremente, este es tu espacio, donde podrás ser tu misma. Para ello, queremos brindarte un servicio de calidad, por lo cual quiero hacerte algunas preguntas las cuales son totalmente  confidenciales y resguardadas en todo momento.')
    bot.send_message(message.chat.id, 'Inicia pulsado aqui para iniciar con la ayuda /test.')


@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.send_message(message.chat.id, 'Puedes interactuar conmigo usando comandos. Por ahora, solo respondo a /start y /help')

@bot.message_handler(commands=['test'])
def cmd_test(message):
    markup= ForceReply()
    msg= bot.send_message(message.chat.id, '¿Como puedo llamarte?', reply_markup=markup)
    bot.register_next_step_handler(msg, nombre_gusto)

def nombre_gusto(message):
    nombre= message.text
    markup= ForceReply()
    msg= bot.send_message(message.chat.id, '¿Como te gusta que te digan?', reply_markup=markup)
    bot.register_next_step_handler(msg, trabajo)

def trabajo(message):
    usuario[message.chat.id]={}
    usuario[message.chat.id]["nombreGusto"]= message.text
    markup= ForceReply()
    msg= bot.send_message(message.chat.id, '¿A que te dedicas?', reply_markup=markup)
    bot.register_next_step_handler(msg, edad)

def edad(message):
    trabajo= message.text
    markup= ForceReply()
    msg= bot.send_message(message.chat.id, '¿Me puedes compartir que edad tienes?', reply_markup=markup)
    bot.register_next_step_handler(msg, estudios)

def estudios(message):
    if not message.text.isdigit():
        markup= ForceReply()
        msg= bot.send_message(message.chat.id, 'ERROR: Debes indicar un numero.', reply_markup=markup)
        bot.register_next_step_handler(msg, estudios)
    else:
        markup= ForceReply()
        msg= bot.send_message(message.chat.id, '¿Cuál es tu ultimo grado de estudio?', reply_markup=markup)
        bot.register_next_step_handler(msg, religion)

def religion(message):
    markup= ForceReply()
    msg= bot.send_message(message.chat.id, '¿Practicas alguna religión?', reply_markup=markup)
    bot.register_next_step_handler(msg, estado_civil)

def estado_civil(message):
    markup= ForceReply()
    msg= bot.send_message(message.chat.id, '¿Cuál es tu Estado civil?', reply_markup=markup)
    bot.register_next_step_handler(msg, pVive)

def pVive(message):
    markup= ForceReply()
    msg= bot.send_message(message.chat.id, '¿Con quien vives?', reply_markup=markup)
    bot.register_next_step_handler(msg, problemas)

def problemas(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    bot.send_message(message.chat.id, 'Consideras que has experimentado en las ultimas semanas problemas en el ámbito: ')
    msg= bot.send_message(message.chat.id, 'Familiar', reply_markup=markup)
    bot.register_next_step_handler(msg, p2)

def p2(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Educativo', reply_markup=markup)
    bot.register_next_step_handler(msg, p3)

def p3(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Laboral', reply_markup=markup)
    bot.register_next_step_handler(msg, p4)

def p4(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Religioso', reply_markup=markup)
    bot.register_next_step_handler(msg, p5)

def p5(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Social', reply_markup=markup)
    bot.register_next_step_handler(msg, problemas2)

def problemas2(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    bot.send_message(message.chat.id, 'En estas últimas semanas has tenido problemas con tu estado de ánimo y afecto en relación a: ')
    msg= bot.send_message(message.chat.id, 'Insegura', reply_markup=markup)
    bot.register_next_step_handler(msg, p6)

def p6(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Impotente', reply_markup=markup)
    bot.register_next_step_handler(msg, p7)

def p7(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Con culpa', reply_markup=markup)
    bot.register_next_step_handler(msg, p8)

def p8(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Frustada', reply_markup=markup)
    bot.register_next_step_handler(msg, p9)

def p9(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Con miedo constante', reply_markup=markup)
    bot.register_next_step_handler(msg, p10)

def p10(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Ansiedad', reply_markup=markup)
    bot.register_next_step_handler(msg, p11)

def p11(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Enojada', reply_markup=markup)
    bot.register_next_step_handler(msg, p12)

def p12(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Desesperanza', reply_markup=markup)
    bot.register_next_step_handler(msg, p13)

def p13(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Tristeza constante', reply_markup=markup)
    bot.register_next_step_handler(msg, problemas3)

def problemas3(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    bot.send_message(message.chat.id, 'En las últimas semanas has experimentado en el área sensoperceptiva y memoria problemas en relación a: ')
    msg= bot.send_message(message.chat.id, 'Alusinaciones', reply_markup=markup)
    bot.register_next_step_handler(msg, p14)

def p14(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Perdidas de recuerdos (amnesia)', reply_markup=markup)
    bot.register_next_step_handler(msg, p15)

def p15(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Recordar situaciones que no han ocurrido (paramsenia)', reply_markup=markup)
    bot.register_next_step_handler(msg, problemas4)

def problemas4(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    bot.send_message(message.chat.id, 'En las últimas semanas has experimentado problemas con tus pensamientos con respecto a: ')
    msg= bot.send_message(message.chat.id, 'Pensamiento suicida', reply_markup=markup)
    bot.register_next_step_handler(msg, p16)

def p16(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Ideas obsesivas', reply_markup=markup)
    bot.register_next_step_handler(msg, problemas5)

def problemas5(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    bot.send_message(message.chat.id, 'Has presentado problemas en las últimas semanas en relación al sueño como, por ejemplo: ')
    msg= bot.send_message(message.chat.id, 'Insomnio', reply_markup=markup)
    bot.register_next_step_handler(msg, p17)

def p17(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Pesadillas recurrentes', reply_markup=markup)
    bot.register_next_step_handler(msg, problemas6)

def problemas6(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    bot.send_message(message.chat.id, 'Últimamente has tenido problemas de comportamiento con respecto a: ')
    msg= bot.send_message(message.chat.id, 'Trastornos alimenticios', reply_markup=markup)
    bot.register_next_step_handler(msg, p18)

def p18(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Autolesión', reply_markup=markup)
    bot.register_next_step_handler(msg, p19)

def p19(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Impulsividad', reply_markup=markup)
    bot.register_next_step_handler(msg, p20)

def p20(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Aislamiento', reply_markup=markup)
    bot.register_next_step_handler(msg, p21)

def p21(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Bajo rendimiento en mis actividades', reply_markup=markup)
    bot.register_next_step_handler(msg, p22)

def p22(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Comerte las uñas (onicofagia)', reply_markup=markup)
    bot.register_next_step_handler(msg, problemas7)

def problemas7(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    bot.send_message(message.chat.id, 'Durante las últimas semanas has presentado dificultades por: ')
    msg= bot.send_message(message.chat.id, 'Dermatitis', reply_markup=markup)
    bot.register_next_step_handler(msg, p23)

def p23(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Problemas digestivos', reply_markup=markup)
    bot.register_next_step_handler(msg, p24)

def p24(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Alteraciones respiratorias', reply_markup=markup)
    bot.register_next_step_handler(msg, p25)

def p25(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Migrañas', reply_markup=markup)
    bot.register_next_step_handler(msg, p26)

def p26(message):
    markup= ReplyKeyboardMarkup(
        one_time_keyboard=True,
        input_field_placeholder="Pusa un boton"
    )
    markup.add("Si","No")
    msg= bot.send_message(message.chat.id, 'Tensión muscular', reply_markup=markup)
    bot.register_next_step_handler(msg, final)

def final(message):
    texto= f'Gracias {usuario[message.chat.id]["nombreGusto"]} por compartir esta información conmigo, te voy a canalizar en este momento con una hermana capacitada que te va a escuchar, fue un gusto para mí que compartieras conmigo esta experiencia.'
    bot.send_message(message.chat.id,texto,parse_mode="html")

#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)



if __name__ == "__main__":
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Iniciar conversación con el bot."),
        telebot.types.BotCommand("/help", "Comandos del bot."),
    ])
    bot.infinity_polling()

