import vk_api, json, random, sqlite3
from vk_api.longpoll import VkLongPoll, VkEventType 
def write_msg(user_id,message, keyboard):
	vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048) , 'keyboard' : keyboard})
token = "706b2d5a9c82d832e04fb62194b22d827e57f094b2022ded1d7756f3aef3dfd6ef9efe82f4d6140bba53d"
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)
def get_but(text,color):
	return {
				"action":{
					"type": "text",
					"payload": "{\"button\": \"" + "1" + "\"}",
					"label":f"{text}"
				},
				"color": f"{color}"
			}
keyboard = {
	"one_time" : False,
	"buttons" : [
		[get_but('создать','positive'), get_but('пройти','positive')],
		[get_but('отмена','positive')]
	]
}
keyboardI = {
	"one_time" : False,
	"buttons" : [
		[get_but('подтвердить','positive')],
		[get_but('отмена','positive')]
	]
}
keyboardII = {
	"one_time" : False,
	"buttons" : [
		[get_but('отмена','positive')]
	]
}
keyboardIII = {
	"one_time" : False,
	"buttons" : [
		[get_but('продолжить','positive')],
		[get_but('завершить','positive')],
		[get_but('отмена','positive')]
	]
}
keyboardIII = {
	"one_time" : False,
	"buttons" : [
		[get_but('продолжить','positive')],
		[get_but('завершить','positive')],
		[get_but('отмена','positive')]
	]
}

keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
keyboardI = json.dumps(keyboardI, ensure_ascii = False).encode('utf-8')
keyboardI = str(keyboardI.decode('utf-8'))
keyboardII = json.dumps(keyboardII, ensure_ascii = False).encode('utf-8')
keyboardII = str(keyboardII.decode('utf-8'))
keyboardIII = json.dumps(keyboardIII, ensure_ascii = False).encode('utf-8')
keyboardIII = str(keyboardIII.decode('utf-8'))

con = sqlite3.connect('vk_bot.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS question (
	id INTEGER,
	id_cretor TEXT,
	text1 TEXT,
	answer1 TEXT,
	text2 TEXT,
	answer2 TEXT,
	text3 TEXT,
	answer3 TEXT,
	text4 TEXT,
	answer4 TEXT,
	text5 TEXT,
	answer5 TEXT);
""")
con.commit()
def answerlisten():
	global text
	global cancel
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			if event.to_me:
				request = event.text
				if request != "отмена":
					text = request
					write_msg(event.user_id, "введите ответ",keyboardII)
					break
				else:
					if cancel == 1:
						break
					else:
						cancel = 1
						write_msg(event.user_id, "удачи",keyboard)
						break
def textlistenI():
	global answer
	global cancel
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			if event.to_me:
				request = event.text
				if request != "отмена":
					answer = request
					write_msg(event.user_id, "введите вопрос",keyboardII)
					break
				else:
					if cancel == 1:
						break
					else:
						cancel = 1
						write_msg(event.user_id, "удачи",keyboard)
						break
def textlisten():
	global cancel
	global text
	global answer
	if cancel !=1:
		answerlisten()
	if cancel !=1:
		textlistenI()
def random_id ():
	global id
	id = 0
	time = 0
	while time < 10:
		number_list = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9']
		time+=1
		id=str(id) + str(random.choice(number_list))
def read_table(id_II):
	global text1
	global answer1
	global text2
	global answer2
	global text3
	global answer3
	global text4
	global answer4
	global text5
	global answer5
	id_III = id_II
	cur.execute("SELECT text1 FROM question WHERE id =" + str(id_III))
	test1 = cur.fetchone()
	text1 = str(str(test1)[2:-3])
	cur.execute("SELECT answer1 FROM question WHERE id =" + str(id_III))
	answer1 = cur.fetchone()
	answer1 = str(str(answer1)[2:-3])
	cur.execute("SELECT text2 FROM question WHERE id =" + str(id_III))
	test2 = cur.fetchone()
	text2 = str(str(test2)[2:-3])
	cur.execute("SELECT answer2 FROM question WHERE id =" + str(id_III))
	answer2 = cur.fetchone()
	answer2 = str(str(answer2)[2:-3])
	cur.execute("SELECT text3 FROM question WHERE id =" + str(id_III))
	test3 = cur.fetchone()
	text3 = str(str(test3)[2:-3])
	cur.execute("SELECT answer3 FROM question WHERE id =" + str(id_III))
	answer3 = cur.fetchone()
	answer3 = str(str(answer3)[2:-3])
	cur.execute("SELECT text4 FROM question WHERE id =" + str(id_III))
	test4 = cur.fetchone()
	text4 = str(str(test4)[2:-3])
	cur.execute("SELECT answer4 FROM question WHERE id =" + str(id_III))
	answer4 = cur.fetchone()
	answer4 = str(str(answer4)[2:-3])
	cur.execute("SELECT text5 FROM question WHERE id =" + str(id_III))
	test5 = cur.fetchone()
	text5 = str(str(test5)[2:-3])
	cur.execute("SELECT answer5 FROM question WHERE id =" + str(id_III))
	answer5 = cur.fetchone()
	answer5 = str(str(answer5)[2:-3])
def user_answert(textI):
	global answer_user
	global cancel
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			if event.to_me:
				request = event.text
				if request != "отмена" and cancel == 0:
					answer_user = request
					write_msg(event.user_id, textI ,keyboardII)
					break
				if request == "отмена" or cancel == 1:
					if cancel == 1:
						break
					elif request == "отмена":
						cancel = 1
						write_msg(event.user_id, "удачи",keyboard)
						break
def check():
	global bl1, bl2, bl3, bl4, bl5
	if answer_user1 == answer1:
		bl1 = "верно"
	else:
		bl1 = "неверно"
	if answer_user2 == answer2:
		bl2 = "верно"
	else:
		bl2 = "неверно"
	if answer_user3 == answer3:
		bl3 = "верно"
	else:
		bl3 = "неверно"
	if answer_user4 == answer4:
		bl4 = "верно"
	else:
		bl4 = "неверно"
	if answer_user5 == answer5:
		bl5 = "верно"
	else:
		bl5 = "неверно"
for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			request = event.text
			t = 0
			if request == "привет" or request == "Привет":
				write_msg(event.user_id, "Я бот для создания и прохождения опросов. \n Создать/Пройти",keyboard)
			elif request == "Создать" or request == "создать":
				request = 0
				cancel = 0
				answer = 0
				text = 0
				write_msg(event.user_id, "введите вопрос",keyboardII)
				textlisten()
				text1 = text
				answer1 = answer
				textlisten()
				text2 = text
				answer2 = answer
				textlisten()
				text3 = text
				answer3 = answer
				textlisten()
				text4 = text
				answer4 = answer
				if cancel !=1:
					for event in longpoll.listen():
						if event.type == VkEventType.MESSAGE_NEW:
							if event.to_me:
								request = event.text
								if request != "отмена" and cancel != 1 :
									text = request
									write_msg(event.user_id, "введите ответ",keyboardII)									
									for event in longpoll.listen():
										if event.type == VkEventType.MESSAGE_NEW:
											if event.to_me:
												request = event.text
												if request != "отмена" and cancel != 1 :
													answer5 = request
													text5 = text
													t=0
													write_msg(event.user_id, "подтвердите создание",keyboardI)
													for event in longpoll.listen():
														if event.type == VkEventType.MESSAGE_NEW:
															if event.to_me:
																request = event.text
																if request == "подтвердить" and cancel != 1 and t == 0:
																	random_id ()
																	cur.execute(f"SELECT id FROM question WHERE id = '{id}'")
																	while t==0:
																		if cur.fetchone() is None:
																			write_msg(event.user_id, "опрос создан \n ваш id: \n " + id ,keyboard)
																			cur.execute(f"INSERT INTO question VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(id, event.user_id, text1, answer1, text2, answer2, text3, answer3, text4, answer4, text5, answer5))
																			con.commit()
																			t = 1
																			break
																		else:
																			random_id ()
																	break
																elif request == "отмена" or cancel == 1 or t == 1:
																	if cancel == 1 or t == 1:
																		break
																	else:
																		cancel = 1
																		write_msg(event.user_id, "удачи",keyboard)
																		break
																else:
																	write_msg(event.user_id, "я вас не понял",keyboardI)
												else:
													if cancel == 1:
														break
													else:
														cancel = 1
														write_msg(event.user_id, "удачи",keyboard)
														break
								else:
									if cancel == 1:
										break
									else:
										cancel = 1
										write_msg(event.user_id, "удачи",keyboard)
										break					
			elif request == "пройти" or "Пройти":
				cancel = 0
				answer_user = 0
				write_msg(event.user_id, "введите id задания",keyboardII)
				for event in longpoll.listen():
					if event.type == VkEventType.MESSAGE_NEW:
						if event.to_me:
							request = event.text
							if request != "отмена" :
								id_I = request
								cur.execute(f"SELECT id FROM question WHERE id = '{id_I}'")
								if cur.fetchone() is None:
									write_msg(event.user_id, "такого задания нету",keyboardII)
								else:
									read_table(id_I)
									write_msg(event.user_id, text1 ,keyboardII)
									for event in longpoll.listen():
										if event.type == VkEventType.MESSAGE_NEW:
											if event.to_me:
												request = event.text
												if request != "отмена" and cancel != 1:
													answer_user1 = request
													write_msg(event.user_id, text2 ,keyboardII)
													if cancel!= 1:
														user_answert(text3)
													answer_user2 = answer_user
													if cancel!= 1:
														user_answert(text4)
													answer_user3 = answer_user
													if cancel!= 1:
														user_answert(text5)
													answer_user4 = answer_user
													if request != "отмена" and cancel != 1:
														for event in longpoll.listen():
															if event.type == VkEventType.MESSAGE_NEW:
																if event.to_me:
																	answer_user = event.text
																	if request != "отмена" and cancel != 1:
																		answer_user5 = answer_user
																		check()
																		write_msg(event.user_id, "Ваш ответ:" + "\n" + " " + answer_user1 + "\n" + "Правильный ответ:" + "\n" + " " + answer1 + "\n" + "задание выполнено:" + "\n" + " " + bl1 ,keyboard)
																		write_msg(event.user_id, "Ваш ответ:" + "\n" + " " + answer_user2 + "\n" + "Правильный ответ:" + "\n" + " " + answer2 + "\n" + "задание выполнено:" + "\n" + " " + bl2 ,keyboard)
																		write_msg(event.user_id, "Ваш ответ:" + "\n" + " " + answer_user3 + "\n" + "Правильный ответ:" + "\n" + " " + answer3 + "\n" + "задание выполнено:" + "\n" + " " + bl3 ,keyboard)
																		write_msg(event.user_id, "Ваш ответ:" + "\n" + " " + answer_user4 + "\n" + "Правильный ответ:" + "\n" + " " + answer4 + "\n" + "задание выполнено:" + "\n" + " " + bl4 ,keyboard)
																		write_msg(event.user_id, "Ваш ответ:" + "\n" + " " + answer_user5 + "\n" + "Правильный ответ:" + "\n" + " " + answer5 + "\n" + "задание выполнено:" + "\n" + " " + bl5 ,keyboard)
																		break
																	elif request == "отмена" or cancel == 1:
																		if cancel == 1:
																			break
																		elif request == "отмена":
																			cancel = 1
																			write_msg(event.user_id, "удачи",keyboard)
																			break
													elif request == "отмена" or cancel == 1:
														if cancel == 1:
															break
														elif request == "отмена":
															cancel = 1
															write_msg(event.user_id, "удачи",keyboard)
															break
												elif request == "отмена" or cancel == 1:
													if cancel == 1:
														break
													elif request == "отмена":
														cancel = 1
														write_msg(event.user_id, "удачи",keyboard)
														break
							elif request == "отмена" or cancel == 1:
								if cancel == 1:
									break
								elif request == "отмена":
									cancel = 1
									write_msg(event.user_id, "удачи",keyboard)
									break
					if request == "отмена" or cancel == 1:
						if cancel == 1:
							break
						elif request == "отмена":
							cancel = 1
							write_msg(event.user_id, "удачи",keyboard)
							break
		elif request == "DeleteProgramUse":
			break
		elif request == "отмена":
			write_msg(event.user_id, "Я бот для создания и прохождения опросов. \n Создать/Пройти",keyboard)
		else:
			write_msg(event.user_id, "я вас не понял",keyboard)