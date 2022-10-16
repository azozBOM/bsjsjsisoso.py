import telebot,requests 
from telebot import types
Token = input("5523757035:AAEB83pwPkYwZ-4fobFY2kz3gIu2Ir4sUvA")
bot = telebot.TeleBot(Token)
ch="𝒄𝒉𝒂𝒏𝒏𝒆𝒍"
dev="𝒅𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓"
key = types.InlineKeyboardMarkup()
A = types.InlineKeyboardButton(text=dev,url="t.me/BEEEB8")
B = types.InlineKeyboardButton(text=ch,url="t.me/php06")
key.add(A,B)
@bot.message_handler(commands=['start'])
def start(message):
	start = """/
*Welcome Bot .*
*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
*- أهلا بك في بوت IP .*

*- لـ معرفة IP الخاص بك أرسل الأمر* /getip *.*

*- لـ معرفة IP لديك أرسل الأمر* /ip + IP *.*
*- - - - - - - - - - - - - *
-مثال : 
`/ip 86.111.151.113`
*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
"""
	bot.send_message(message.chat.id,start,parse_mode="Markdown",reply_markup=key)
@bot.message_handler(func=lambda message: True)
def getip(message):
	try:
		if message.text == "/getip":
			u = requests.get("https://ipinfo.io/json").json()
			ip = u['ip'];city = u['city']
			pro = u['region'];country = u['country']
			loc = u['loc'];zone = u['timezone']
			get = f"""Your IP Phone 
*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
*IP :* `{ip}`
*TimeZone :* `{zone}`
*Country :* `{country}/{pro}`
*City :* `{city}`
*Lociton :* `{loc}`
*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
""" 
			bot.reply_to(message,get,parse_mode="Markdown",reply_markup=key)
		
		# # # # # 
		ID = message.from_user.id 
		msg = message.text
		if "/ip " in msg :
			msg = msg.split('/ip ')[1]
			print(msg)
			r = requests.get(f"http://ip-api.com/json/{msg}").json()
			iq = r['query'];country = r['country']
			Ccode = r['countryCode'];city = r['city']
			pro = r['regionName'];zone = r['timezone']
			all = f"""
*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
*IP* = `{iq}`
*Country Code* : `{Ccode}`
*TimeZone* : `{zone}`
*County* : `{country}/{pro}`
*City :* `{city}`
*- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -*
"""
			bot.send_message(message.chat.id,all,parse_mode="Markdown", reply_markup=key)
		else:
			bot.send_message(message.chat.id, "Error IP ..!")
	except : pass

bot.polling(True)