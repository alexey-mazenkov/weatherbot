# Weather Bot v0.0.1.
# Deverloper - Mazenkov Alexey

import pyowm  # Importing module with weather data.
owm = pyowm.OWM('8e2f4534df1cbcb6300fc8fa009f4f4e', language='ru')

import telebot  # Importing module with TelegramBot API
bot = telebot.TeleBot('828439192:AAH-0ngnJwu_4rxZgKTc_CV5RslHTP4puDo')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Погоду в каком городе Вам нужно узнать?")    # Welcome message.

@bot.message_handler(content_types=['text'])
def answer(message):

    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    wind = w.get_wind()['speed']     # Get wind speed
    humidity = w.get_humidity()     # Get humidity.
    temp = w.get_temperature('celsius')['temp']     # Get temperature in celsius.

    issue = "В городе " + message.text + " сейчас:" + "\n"
    issue += "Температура: " + str(temp) + " C°" + "\n"
    issue += "Влажность: " + str(humidity) + " %" + "\n"
    issue += "Скорость ветра: " + str(wind) + " м/с"

    bot.send_message(message.chat.id, issue)    # Bot send message.

bot.polling(none_stop=True)


