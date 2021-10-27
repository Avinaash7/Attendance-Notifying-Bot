import time
import telebot
import speech_recognition as sr

API_KEY = '2026898662:AAHmVmpjx7e1El99JgahWL-AmjbzvCtDcBw'
bot = telebot.TeleBot(API_KEY)
r = sr.Recognizer()
run = True

name = input("Enter your First Name:- ")  # The Name with which your teacher might call you
device_in = int(input("Enter Device Index:- "))  # The device index you get from device_index_finder file


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Peacefully sleep or do something, I will notify when there's attendance or if someone call's you.")
    while run:
        with sr.Microphone(device_index=device_in) as source:
            time.sleep(2)
            print("Listening..")
            audio_text = r.listen(source)
            print("Done")
            try:
                text = r.recognize_google(audio_text)
                print(r.recognize_google(audio_text))
                if "attendance" in text:
                    bot.send_message(message.chat.id, "Attendance Started !!")
                if name.lower() in text:
                    bot.send_message(message.chat.id, "You are being Called !!")
            except sr.UnknownValueError:
                print("Google could not understand audio")
            except sr.RequestError as e:
                print("Google error; {0}".format(e))


@bot.message_handler(commands=['stop'])
def stop_bot(message):
    bot.reply_to(message,
                 "Bye, Until next class !!")
    bot.stop_poll(message.chat.id, message.id)


bot.polling()
