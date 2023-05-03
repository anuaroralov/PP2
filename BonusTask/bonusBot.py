import telebot
import psycopg2
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)   

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        limit1 INTEGER NOT NULL,
        total INTEGER DEFAULT 0
    );
""")
conn.commit()

bot = telebot.TeleBot("6122895026:AAFZAnME9ume_Qn3Dla6BODHT9w_XJ0a9iU")

menu_commands = [
    telebot.types.BotCommand('start', 'Start the bot'),
    telebot.types.BotCommand('help', 'узнать команды'),
    telebot.types.BotCommand('add_goal', 'добавить новую цель'),
    telebot.types.BotCommand('add_savings', 'добавить сбережение к цели'),
    telebot.types.BotCommand('check_goal', 'проверить текущее значение цели'),
    telebot.types.BotCommand('delete_goal', 'удалить цель')
]
bot.set_my_commands(menu_commands)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "Привет! Я бот-копилка. Я помогу тебе следить за твоими целями и сбережениями. Доступные команды: /help"
    bot.reply_to(message, text)
    
@bot.message_handler(commands=['add_goal'])
def add_goal(message):
    bot.reply_to(message, "На что вы хотите накопить?")

    bot.register_next_step_handler(message, get_goal_name)


def get_goal_name(message):
    name = message.text

    # Запросить лимит цели
    bot.reply_to(message, "Сколько тг надо накопить?")

    # Регистрируем следующий обработчик на получение лимита цели
    bot.register_next_step_handler(message, get_goal_limit, name)

def get_goal_limit(message, name):
    limit1 = message.text
    
    # Вставить цель в базу данных
    cursor = conn.cursor()
    sql = "INSERT INTO goals (name, limit1) VALUES (%s, %s)"
    cursor.execute(sql, (name, int(limit1)))
    conn.commit()
    
    bot.reply_to(message, "Цель успешно добавлена!")

@bot.message_handler(commands=['add_savings'])
def add_savings(message):
    # Запросить название цели
    bot.reply_to(message, "К какой цели относится ваше сбережение?")

    # Регистрируем следующий обработчик на получение названия цели
    bot.register_next_step_handler(message, get_savings_goal)

def get_savings_goal(message):
    name = message.text

    # Запросить сумму к цели
    bot.reply_to(message, "Какую сумму вы хотите добавить к этой цели?")

    # Регистрируем следующий обработчик на получение суммы
    bot.register_next_step_handler(message, get_savings_amount, name)

def get_savings_amount(message, name):
    amount = message.text

    # Найти цель в базе данных и обновить ее
    sql = "SELECT * FROM goals WHERE name = %s"
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    if result:
        new_total = result[3] + int(amount)
        if new_total > result[2]:
            bot.reply_to(message, f"Превышен лимит цели '{name}'! Было добавлено только {result[2] - result[3]} тг")
            new_total = result[2]
        else:bot.reply_to(message, "Сумма успешно добавлена к цели!")
        sql = "UPDATE goals SET total = %s WHERE name = %s"
        cursor.execute(sql, (new_total, name))
        conn.commit()
    else:
        bot.reply_to(message, "Цель не найдена.")

@bot.message_handler(commands=['check_goal'])
def check_goal(message):
    # Запросить название цели
    bot.reply_to(message, "Название цели:")

    # Регистрируем следующий обработчик на получение названия цели
    bot.register_next_step_handler(message, get_goal_total)
    
def get_goal_total(message):
    name = message.text

    # Найти цель в базе данных и вывести ее текущее значение
    sql = "SELECT * FROM goals WHERE name = %s"
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    if result:
        bot.reply_to(message, f"Текущая сумма для цели '{name}': {result[3]}")
    else:
        bot.reply_to(message, "Цель не найдена.")

@bot.message_handler(commands=['delete_goal'])
def remove_goal(message):
    # Запросить название цели
    bot.reply_to(message, "Название цели:")

    # Регистрируем следующий обработчик на получение названия цели
    bot.register_next_step_handler(message, delete_goal)

def delete_goal(message):
    name = message.text

    # Удалить цель из базы данных
    cursor = conn.cursor()
    sql = "DELETE FROM goals WHERE name = %s"
    cursor.execute(sql, (name,))
    conn.commit()

    # Отправить ответ пользователю
    if cursor.rowcount == 1:
        bot.reply_to(message, f"Цель '{name}' успешно удалена.")
    else:
        bot.reply_to(message, "Цель не найдена.")

@bot.message_handler(commands=['help'])  
def help_command(message):  
    text = "/add_goal - добавить новую цель\n"
    text += "/add_savings - добавить сбережение к цели\n"
    text += "/check_goal - проверить текущее значение цели\n"
    text += "/delete_goal - удалить цель\n"
    text += "/help - список доступных команд\n"
    bot.reply_to(message, text)

bot.polling()
