from constants import API_KEY
import telebot
from telebot import custom_filters

from telebot.handler_backends import State,StatesGroup
from telebot.storage import StateMemoryStorage
import openai
state_storage = StateMemoryStorage()

bot = telebot.TeleBot(API_KEY,parse_mode=None,state_storage=state_storage)
password="evolvestech2023"
class MyStates(StatesGroup):
    started=State()
    verified=State()
    




def answer_from_gpt(ask):
	openai.api_key = "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"
	response = openai.Completion.create(
	model="text-davinci-003",
	prompt=ask,
	temperature=0.9,
	max_tokens=1000,
	top_p=1,
	frequency_penalty=0,
	presence_penalty=0.6,
	stop=[" Human:", " AI:"]
	)
	text = response['choices'][0]['text']
	return text


@bot.message_handler(commands=['start'])
def send_welcome(msg):
	bot.set_state(msg.from_user.id, MyStates.started, msg.chat.id)
	bot.send_message(chat_id=msg.chat.id,text="I was created by evolves.tech, please ask me anything. I can code, write and inspire you, try me out.")
	bot.send_message(chat_id=msg.chat.id,text="please enter password ?")


@bot.message_handler(state=MyStates.started)
def send_welcome(msg):
	print("working congra")
	print(msg.chat.id)
	pas=msg.text
	if pas =="evolvestech2023":
		bot.set_state(msg.from_user.id, MyStates.verified, msg.chat.id)
		bot.send_message(chat_id=msg.chat.id,text="you have succesfully logged in you can ask ")
	else:
		bot.send_message(chat_id=msg.chat.id,text="password is incorrect please enter again ?")


@bot.message_handler(state=MyStates.verified,func=lambda message : True)
def send_welcome(msg):
	answer=answer_from_gpt(msg.text)
	bot.send_message(chat_id=msg.chat.id,text=answer)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.infinity_polling()