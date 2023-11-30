import telebot
from telebot import types

bot = telebot.TeleBot('TOKEN BOT')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Hi, People!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я  Бот-Векторина!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Hi, People!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Вы любите животных?')
        #btn2 = types.KeyboardButton('Правила сайта')
        #btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '❓ Давайте поиграем Вопросы-Ответы', reply_markup=markup) #ответ бота


    elif message.text == 'Вы любите животных?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Подумай хорошо', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('А Вы знаете кто такие млекопитающие?')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Отлично, следующий вопрос', reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Ясно вижу Вам нравятся Рыбки?' )
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Нечего, сейчас мы окунемся в океан', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'А Вы знаете кто такие млекопитающие?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да, в полне ')
        btn2 = types.KeyboardButton('Нет, смутно')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Очень хорошо! ', reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Да, в полне':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Ягуарунди')
        btn2 = types.KeyboardButton('Лама')
        btn3 = types.KeyboardButton('Японский макак')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Тогда вам известны эти виды:', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Ягуарунди':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном' )
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, """Ягуарунди обитает почти на всей территории Южной Америки, 
за исключением западной горной местности и самого юга континента. Ареал охватывает и Центральную Америку.
Ягуарунди предпочитают жить в густых лесах, среди кустарников, встречаются в болотистых местностях, 
даже в горах до 3000 м над уровнем моря. Особенности строения тела позволяют 
им с лёгкостью пробираться среди густой травы и переплетения ветвей.
Внешний вид и морфология.
Внешность у ягуарунди очень своеобразная: небольшая голова, вытянутое, гибкое, 
в то же время довольно массивное туловище, короткие ноги и очень длинный хвост. 
Длина тела этой кошки 55 - 77 см, хвоста – до 60 см, высота в холке около 25-35 см, вес 4,5-9 кг. 
В целом, ягуарунди немного похожа на мадагаскарскую фоссу.
Окраска разных особей от рыжей до почти черной, однотонная, 
лишь на мордочке возле носа и на груди шерсть чуть светлее общего фона. 
У новорожденных котят иногда бывает крапчатая окраска. Шерстный покров густой, но короткий."""  + """ (https://moscowzoo.ru/upload/iblock/a95/a95c0e1c18f051933644368bb2bc2350.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Ягуанини став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! 
""", parse_mode='Markdown',reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #btn1 = types.KeyboardButton(' ?')
        #markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по'  + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')

    elif message.text == 'Лама':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Поскольку лама ведёт свою родословную от гуанако, 
 то и похожа она больше всего на это животное. Такая же грациозная, пропорциями напоминающая больше оленя, чем верблюда. 
 Чуть более массивная и крупная, чем дикий предок: высота в холке в среднем 120 см, высота до темени — 180 см. 
 Но вот окраска шерсти может быть самой разнообразной — от чисто белой до тёмно-бурой, как однотонной, так и пегой. 
 Шерсть очень густая, длинная, как и положено жителю сурового высокогорья. Высоко поднятая голова на длинной шее придаёт этому зверю немного «высокомерное» выражение, 
 которое подчеркивается большими глазами, обрамлёнными густыми ресницами. Самцы несколько крупнее самок. """ + """ (https://moscowzoo.ru/upload/iblock/813/02.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Ламе став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id,'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)',parse_mode='Markdown')


    elif message.text == 'Японский макак':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Японский макак отличается крепким сложением и мощными конечностями. 
    По весу он тяжелее других видов макак; самцы весят в среднем 11 кг при росте 80-95 см, самки ниже, и вес в среднем – 9 кг. 
    Мех довольно длинный, на зиму отрастает густой подшерсток. Окраска у разных животных имеет приятные оттенки от коричневато-серого через серовато-голубой до буро-оливкового; 
    живот окрашен в более светлые тона. Шерсть на передних конечностях, плечах и спине длиннее, чем на других частях тела, а на груди и животе шерстный покров менее развит.
Хвост не более 10 см; седалищные мозоли, характерные для макак и мартышек, небольшие. Имеются защёчные мешки, 
которые представляют собой две внутренние складки по обеим сторонам рта, образующие кожные выросты, направленные вниз и свисающие до уровня подбородка. 
Кожа, светлая на всём теле, на лице и около хвоста приобретает интенсивно розовый и даже красный цвет, когда обезьяна становится взрослой. 
Половые различия у взрослых животных хорошо заметны, несмотря на то, что представители обоих полов носят бороду и бакенбарды, – самцы массивнее самок.
Глаза защищены надбровными дугами, более выраженными у самцов. Из всех органов чувств наиболее развито зрение. 
Оно, как и у человека, стереоскопическое, что означает, что макак видит объёмное изображение и оценивает расстояние.
Конечности пятипалые, большие пальцы и на руках, и на ногах противопоставлены остальным, что позволяет как держаться за всевозможные предметы, 
так и совершать с ними довольно тонкие манипуляции. Наиболее развитой частью мозга является кора больших полушарий. """ + """ (https://moscowzoo.ru/upload/iblock/baf/baff93082f9a00cd9aaa88d9f9bbd53d.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Японской макаке став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id,'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)',parse_mode='Markdown')


    elif message.text == 'Нет, смутно':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Вам знакомы Рептилии' )
        markup.add(btn1)
        bot.send_message(message.from_user.id, """Ну что же, и здесь есть выход!Продолжим изучать Фауну планета Земля.
Зоологи и палеонтологи используют термин "фауна" для обозначения типичной коллекции животных, 
найденных в определенное время или в определенном месте""", reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Вам знакомы Рептилии':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да, ооо да ')
        btn2 = types.KeyboardButton('Нет, мммм ')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Очень хорошо! ', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Да, ооо да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Обыкновенная игуана')
        btn2 = types.KeyboardButton('Слоновая черепаха')
        btn3 = types.KeyboardButton('Поющая индийская кобра')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Тогда вам известны эти виды:', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Обыкновенная игуана':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Обыкновенная игуана – достаточно крупная ящерица, длина тела вместе с хостом достигает обычно 1,5 м, хотя известны особи длиной более 2 м и весом свыше 8 кг. 
        В среднем же масса самцов около 4 кг, а самок – от 1,2 до 3 кг. Вес детёнышей при вылуплении из яиц около 12 г, длина варьирует от 17 до 25 см.
Вопреки названию, цвет этой игуаны не обязательно зеленый и зависит от возраста животного и района обитания. В разных частях ареала они могут быть голубоватыми и синими, 
бледно-лиловыми и черными, розовыми, оранжевыми и даже красными.
Тело тонкое, хвост очень длинный и сжатый с боков. На спине и  хвосте хорошо заметен большой продольный гребень, 
защищающий животное от врагов. Голова четырехгранная, покрыта щитками. На горле имеется большой мешок, играющий большую роль в терморегуляции, 
а также в брачном поведении самцов. Зубы у игуаны очень острые, широкие и плоские с мелкими зубчиками по краям. Расположены они на внутренней стороне челюстных костей, 
поэтому их трудно увидеть, особенно у молодых и некрупных особей. С формой зубов игуаны связано название одного из ископаемых ящеров. 
Когда в ХIХ веке были найдены зубы какой-то древней рептилии, исследователи по форме зубов отнесли ее к гигантской игуане и назвали игуанодон (игуанозубый). 
Позже выяснилось, что близкого родства между этими рептилиями нет, но название осталось.
Лапы короткие с длинными пальцами и острыми когтями; и на передних, и на задних конечностях по 5 пальцев.
Как и большинство ящериц, спасаясь от врагов, игуаны отбрасывают хвост, который потом отрастает заново. """ + """ (https://moscowzoo.ru/upload/iblock/ec5/ec505af85c62f877051f160bb2449228.jpg).
Это Ваше Тотемное животное.
Вы можите помочь Обыкновенной ягуане став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id,'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')

    elif message.text == 'Слоновая черепаха':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Слоновая черепаха – самая крупная среди современных сухопутных черепах, 
ее вес может достигать 400 кг, а длина – более 1,8м.
В разных подвидах слоновой черепахи существуют различия в размерах и форме панциря – карапакса. 
По этому признаку они делятся на 2 основные группы: 1) на небольших засушливых островах черепахи более мелкие с седловидным панцирем. 
Ноги у них более длинные и тонкие. Вес самок до 27 кг, самцов – до 54 кг. 2) на крупных островах с более влажным климатом и обильной растительностью черепахи крупнее, 
их панцири высокие и куполообразные. Разница в размерах самок и самцов выражена не так резко.
Отсутствие хищников на островах привело к тому, что панцирь слоновой черепахи широко открыт спереди. 
Благодаря такому панцирю черепахи могут доставать даже довольно удаленные ветки, еще не объеденные другими животными. 
Возможно также, что такая «открытость» панциря способствует лучшей вентиляции тела в условиях жизни в тропиках.  """ + """ (https://laplaya-rus.ru/wp-content/uploads/c/2/e/c2e27af5f787e6b99606afb5e9311d42.jpeg).
Это Ваше Тотемное животное.
Вы можите помочь Слоновой черепахе став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id,'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)',parse_mode='Markdown')




    elif message.text == 'Поющая индийская кобра':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Змея очень опасна и ядовита. Общая длина достигает 1,3 м, максимальная длина — 1,8 м.
Голова эллиптическая, широкая, немного отделена от шеи. Морда короткая, округлая, ноздри большие.
Глаза умеренного размера, зрачок круглый. Окраска одноцветная — чёрная, коричневая или тёмно-серая.
Характерный капюшон, светлый с брюшной стороны, состоит из ребёр. У молодых змей могут присутствовать тёмные пятна или полосы.
Иногда на капюшоне может встречаться тёмный рисунок в форме очков, лошадиной подковы или буквы «О».
Активна как днём, так и ночью. Охотится на мелких млекопитающих, вроде мышей и крыс, а также поедает лягушек,
ящериц и змей, но очень часто змея сама становится добычей для такого страшного хищника, как комодский варан.
Яйцекладущая змея. Спаривание происходит во время сухого сезона (с августа по октябрь). Самка откладывает от 16 до 36 яиц.
Молодые кобры появляются через 88 дней.
Этот вид кобры обитает на индонезийских островах Ява и Малых Зондских островах Бали,
Ломбок, Сумбава, Комодо, Флорес, Ломблен и Алор. Возможно, они могут встречаться и на других островах .  """ + """ (https://gorodprizrak.com/wp-content/uploads/2023/06/5d2225ea61dddfb18a4d8bfe9c4ed634.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Поющей индийской кобре став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')


    elif message.text == 'Нет, мммм':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Птички то, Вам точно знакомы')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'И на этот раз все будет в порядке', reply_markup=markup,
                         parse_mode='Markdown')


    elif message.text == 'Птички то, Вам точно знакомы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Полетели')
        btn2 = types.KeyboardButton('Hi, People!')
        btn3 = types.KeyboardButton('Вылет отменили')
        markup.add(btn1, btn2,btn3)
        bot.send_message(message.from_user.id, """ На сегодняшний день людям известно 10 694 вида птиц, которые живут на Земле.
Единственная в мире птица, которая вообще не имеет крыльев – это киви.
Сердце птицы бьется 1000 раз в минуту во время полета и 400 раз в минуту во время отдыха.
Совы не могут двигать глазами по сторонам. Они поворачивают голову целиком. """, reply_markup=markup, parse_mode='Markdown')




    elif message.text == 'Вылет отменили':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(' ?')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас, что прошли векторину! Данные использованные в векторине были взяты с сайта Московского Зоопарка. Более подробно с обилием Животного мира вы можите ознакомиться на сайте пройдя по ' + '[ссылке](https://moscowzoo.ru/)', parse_mode='Markdown')





    elif message.text == 'Полетели':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Розовый какаду')
        btn2 = types.KeyboardButton('Обыкновенный павлин')
        btn3 = types.KeyboardButton('Малый или тундровый лебедь')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Тогда вам известны эти виды:', reply_markup=markup, parse_mode='Markdown')



    elif message.text == 'Розовый какаду':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Розовый какаду – попугай среднего размера: длина тела – 35-36 см, 
вес около 345 г - у самцов и 311 г - у самок. Внешне розовый какаду отличается от своих собратьев. 
В его окраске характерен контраст между яркими головой и брюхом и темными спиной, крыльями и хвостом. 
Верхняя часть головы у него светло-розовая, ниже уровня глаз – розовато-красная. 
В такой же розовато-красный цвет окрашены горло, зоб, грудь и брюхо. Спина и крылья пепельно-серые, 
маховые и рулевые перья бурые, подхвостье белое. На голове имеется небольшой хохол или гребень. 
Клюв светло-серый, неоперенные участки кожи вокруг глаз голубоватые или розовые, ноги темно-бурые. 
Радужка темно-коричневая у самцов и розовая у взрослых самок, у молодых птиц обоего пола радужка коричневая.
Выделяемые 3 подвида розового какаду отличаются по размерам, тональности окраски оперения и окраске окологлазничных колец. """ + """ (https://moscowzoo.ru/upload/iblock/de9/de922f88e3a90fc5625b942a774a1c75.jpg).
Это Ваше Тотемное животное.
Вы можите помочь Монгольской жабе став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')



    elif message.text == 'Обыкновенный павлин':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Павлины - одни из самых крупных представителей отряда курообразных и, 
        как практически все курообразные, характеризуются четко выраженным половым диморфизмом, т.е. внешним различием 
        самцов и самок. Самцы и крупнее, и значительно ярче окрашены, чем самки.
  Длина тела самца 180-230 см, хвоста – 40-50 см, удлиненных, украшенных «глазками» перьев – 120-160 см, 
размах крыльев – 160 см, вес – 4-6 кг. Самка (пава) бывает длиной 90-100 см, весит 2,7-4 кг. Голова, шея и грудь самца синие, 
спина зеленая, низ тела черный. То, что в просторечии называют «хвостом» павлина – на самом деле удлиненные перья надхвостья. 
Они образуют шлейф из рассученных на большую часть длины перьев бронзово- и золотисто-зеленой окраски с металлически 
блестящими сине-оранжево-фиолетовыми глазками и треугольными изумрудными косицами. Именно эти перья самцы так эффектно раскрывают и играют ими перед самками (а заодно и перед нами). 
Самки павлинов окрашены значительно скромнее и не имеют столь роскошных удлиненных перьев надхвостья.
Домашние павлины тяжелее и у них более короткие ноги.    """ + """ (https://moscowzoo.ru/upload/iblock/aa0/aa0c9262cfc573d917026f25df2f34d8.jpg).
    Это Ваше Тотемное животное.
    Вы можите помочь Монгольской жабе став ее опекуном, находящимся в Московском зоопарке.
    ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')




    elif message.text == 'Малый или тундровый лебедь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Малый лебедь — самый мелкий из всех лебедей, длина тела у него 115–127 см, 
размах крыльев 170–195 см, вес 5–6 кг. Оперение белое, клюв черный с желтым пятном у основания, лапы черные.
Малый лебедь гнездится в зоне тундр от Кольского полуострова до запада Чукотки. 
Таким образом, он является эндемиком России (эндемичный вид имеет ареал, ограниченный строго определенной, часто небольшой территорией).
Сейчас выделяют западную и восточную популяции, причем некоторые орнитологи считают их даже разными подвидами. 
Западная популяция гнездится в тундре от Кольского полуострова до побережья Таймыра, включая полуостров Канин, Югорский полуостров, 
Ямал и Гыданский полуостров. Восточная популяция населяет приморские тундры от низовьев Лены до Чаунской низменности на Чукотке.
Гнездовой биотоп тундрового лебедя — заболоченные и травянистые низины с озерами.""" + """ (https://moscowzoo.ru/upload/iblock/b32/1.jpg).
Это Ваше Тотемное животное.
Вы можите помочь Монгольской жабе став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id,'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)',parse_mode='Markdown')





    elif message.text == 'Ясно вижу Вам нравятся Рыбки?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да, ой да')
        btn2 = types.KeyboardButton('Нет, чтоо?')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Как ранообразен и богат Океанический вид:
а Вы знали что:
Караллы производят свое собственное солнцезащитное средство!
Слишком большое количество солнечного света может повредить водоросли, 
обитающие в кораллах на мелководье. Чтобы защитить водоросли, 
которые являются основным источником их существования, кораллы флуоресцируют. 
В результате они производят белки, которые действуют как своего рода солнцезащитный крем для водорослей.""", reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Да, ой да':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Крылатка-зебра')
        btn2 = types.KeyboardButton('Момбасская крылатка')
        btn3 = types.KeyboardButton('Ложный клоун')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Тогда вам известны эти виды:', reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Крылатка-зебра':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Длина тела до 25 см. В спинном плавнике 13 колючих лучей и 10-11 мягких;
в анальном плавнике 3 колючих луча и 6-7 мягких. В грудном плавнике 16-17 лучей, верхние из которых раздвоены. 
Грудные плавники имеют округлую форму. Ухаживание и нерест у крылатки-зебры начинаются через 20 - 40 минут после захода солнца и 
происходят каждые сутки в течение недели полулунного цикла. Самцы проявляют исключительную агрессивность перед нерестом, 
и схватки между ними в борьбе за территорию часто сопровождаются ранениями, наносимыми лучами спинного плавника. 
В этот период самцы атакуют даже людей-ныряльщиков, вторгающихся на их территорию. Доминирующий самец приобретает темную окраску и патрулирует обширный территориальный участок, 
с которого изгоняет остальных самцов. Он ухаживает за всеми самками, обитающими на охраняемой территории. Во время нереста икра выметывается в две порции, 
каждая из которых заключена в слизистый матрикс шаровидной формы диаметром 2 - 5 см. Такие шары содержат от 2000 до 15000 икринок. Они всплывают и впоследствии распадаются, высвобождая икру. """ + """ (https://moscowzoo.ru/upload/iblock/4b0/4b061147344f0e191b288a4e4ec8b1a1.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Крылатка-зебра став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id,'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)',parse_mode='Markdown')


    elif message.text == 'Момбасская крылатка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Длина тела до 19 см. В спинном плавнике 13 колючих лучей и 10 мягких; 
в анальном плавнике 3 колючих луча и 6 - 7 мягких. 
В грудном плавнике 18 - 20 лучей. 
Верхние и средние лучи грудного плавника сильно удлинены; 
наиболее длинные из них достигают основания хвостового плавника или 
заходят за него. Высота самого длинного луча спинного плавника несколько меньше высоты тела.
Рыбы обитают в тропических водах Индийского и Тихого океанов от Южной Африки до Индонезии, 
Новой Гвинеи и северо-западного побережья Австралии.
Встречаются на коралловых рифах и скальных грунтах, на глубинах более 20 м. """ + """ (https://moscowzoo.ru/upload/iblock/c5e/c5ec2bf6389848158626c1750ab903e0.jpg).
Это Ваше Тотемное животное.
Вы можите помочь Момбасская крылатка став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id,'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)',parse_mode='Markdown')


    elif message.text == 'Ложный клоун':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Длина тела до 9 см. В спинном плавнике 10-11 колючих лучей и 13-17 мягких; 
в анальном плавнике 2 колючих луча и 11-13 мягких. В грудном плавнике 16-18 лучей. На голове, 
в средней части туловища и на хвостовом стебле вертикальные белые полосы. Туловищная полоса имеет треугольную форму.  
Ареал вида включает воды Андаманских и Никобарских о-вов, Индо-Малайского архипелага, северного побережья Австралии, 
Филиппин, побережья Юго-Восточной Азии, Тайваня и южных о-вов Рюкю. 
Рыбы живут на коралловых рифах до глубины 15 м в симбиозе с актиниями Heteractis magnifica, 
Stichodatyla gigantean и S. mertensii. """ + """ (https://moscowzoo.ru/upload/iblock/feb/feb5b1a89f736e5bc754f899802c2093.jpg).
Это Ваше Тотемное животное.
Вы можите помочь Ложный клоун став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id,'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)',parse_mode='Markdown')



    elif message.text == 'Нет, чтоо?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('А Вы знакомы с Амфибиями?' )
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Очень даже хорошо потомучто для Вас есть сюрприз', reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'А Вы знакомы с Амфибиями?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Что то знакомое, Да, вспомнил(а) ')
        btn2 = types.KeyboardButton('О чем Вы говорите, ну Нет')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """Здесь Вас ожидает приятное знакомство с нашими Амфибиями.
Итересный факт об Амфибиях.
Предками амфибий были кистепёрые рыбы, которые по каким-то причинам  выбрались из водной среды на 
сушу около 385 миллионов лет назад. Всего в мире существует порядка 7700 видов амфибий. 
У многих земноводных на темени есть третий глаз, затянутый тонкой кожей. 
Он помогает им определять направление на источник света и ориентироваться в пространстве.
""", reply_markup=markup, parse_mode='Markdown')




    elif message.text == 'Что то знакомое, Да, вспомнил(а)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Монгольская жаба')
        btn2 = types.KeyboardButton('Обыкновенная или серая жаба')
        btn3 = types.KeyboardButton('Зеленая жаба')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Тогда вам известны эти виды:', reply_markup=markup,
                         parse_mode='Markdown')


    elif message.text == 'Монгольская жаба':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Некрупная жаба, длина тела 40-90 мм. За глазами продолговатые железы – паротиды. 
Кожа спины с округлыми бугорками. Окраска крайне изменчива. Пятна образуют сложный изменчивый рисунок, особенно выраженный у взрослых самок. Вдоль середины тела проходит светлая полоса. 
Тёмные пятна, чаще коричневого или каштанового, иногда тёмно-оливкового или зеленовато-серого цвета, блёклые, расположены на значительно более светлом фоне палевого, бежевого, светло-коричневого, светло-серого, реже золотистого цвета. 
Иногда пятна покрывают почти всю поверхность спины. Помимо крупных бородавок на теле, часто внутри пятен, есть мелкие бугорки преимущественно красного цвета. 
Снизу окраска серо-белого или желтоватого цвета, пятна на горле и брюхе встречаются редко. В целом окраска этой жабы может колебаться от светло-песочного до тёмно-оливкового в зависимости как от состояния особей, 
так и характера местообитания.  """ + """ (https://moscowzoo.ru/upload/iblock/8ab/8ab7277e43662487db27fddfa224a0f9.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Монгольской жабе став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')



    elif message.text == 'Обыкновенная или серая жаба':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Крупная жаба, длина тела 50-130 мм, в средиземноморских популяциях – до 200 мм. 
 За глазами продолговатые железы – паротиды. Кожа спины с округлыми бугорками. Сверху светло-серая, серая, коричневая или оливково-бурая. 
Брюхо светло-серое или грязно-белое с темными пятнами. Самцы от самок отличаются стройным телосложением, 
небольшой головой и брачными мозолями на 1-3 пальцах передних конечностей. 
Вид широко распространен в Европе, Северной Азии, отдельные популяции – в Северной Африке и Малой Азии.
В России населяет лесную зону от западных рубежей страны до Прибайкалья на востоке.
Встречается в хвойных, широколиственных и смешанных лесах, рощах, парках и садах. 
На юге ареала заселяет островные леса, кустарники, виноградники и луга.""" + """ (https://moscowzoo.ru/upload/iblock/637/637a1b141efa83ebb02fcf2ba3b4085f.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Обыкновенная или серая жаба став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')



    elif message.text == 'Зеленая жаба':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Жаба средних размеров; максимальная длина до 120 мм. 
Кожа сверху покрыта гладкими бугорками и острыми шипиками (у самцов). За глазами расположены вытянутые железы – паротиды.
Верхняя часть тела светло-серая, иногда бежевая или зеленоватая, с крупными четко очерченными темно-зелеными пятнами различной формы. 
Рисунок окраски очень изменчив. Низ тела беловатый, с пятнами или без них. 
Населяет обширную территорию северо-восточной Африки, Европу и Азию до Сибири и Средней Азии. 
На территории Российской Федерации северная граница ареала совпадает с северной границей подзоны смешанных лесов и
проходит  через Псковскую, Вологодскую, Вятскую и Пермскую области, Средний Урал на юго-восток до Алтая.""" + """ (https://moscowzoo.ru/upload/iblock/dd7/dd72bd84f98177b481f33120aecaf108.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Зеленая жаба став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')





    elif message.text == 'О чем Вы говорите, ну Нет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('А как вам Беспозвоночные?')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'И в этом ответе кроется много загадочных существ', reply_markup=markup,
                         parse_mode='Markdown')


    elif message.text == 'А как вам Беспозвоночные?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Прекрасно знакомы')
        btn2 = types.KeyboardButton('Hi, People!')
        btn3 = types.KeyboardButton('Уж очень они скольские')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, """Этот раздел посвещен прекрасным созданиям: Беспозвоночные.
Интересные факты:
ервые представители беспозвоночных появились на Земле около 1 млрд лет назад. 
А около 600 млн лет назад первые из них в ходе эволюции обзавелись экзоскелетами.
Большинство беспозвоночных настолько отличаются друг от друга, что не имеют между собой практически ничего общего
    """, reply_markup=markup, parse_mode='Markdown')



    elif message.text == 'Уж очень они скольские':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(' ?')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас, что прошли векторину! Данные использованные в векторине были взяты с сайта Московского Зоопарка. Более подробно с обилием Животного мира вы можите ознакомиться на сайте пройдя по ' + '[ссылке](https://moscowzoo.ru/)', parse_mode='Markdown')




    elif message.text == 'Прекрасно знакомы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Четырехцветная актимия')
        btn2 = types.KeyboardButton('Павлиноглазка атлас')
        btn3 = types.KeyboardButton('Совинная бабочка')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Тогда вам известны эти виды:', reply_markup=markup, parse_mode='Markdown')


    elif message.text == 'Четырехцветная актимия':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Данный вид распространен в тропической зоне океана от 
Красного моря и восточного побережья Африки до восточных побережий Меланезии и Микронезии. 
Встречается на коралловых рифах и каменистых грунтах от уреза воды до глубины 40 м. 
Щупальца могут быстро менять свою форму, превращаясь из вытянутых в шаровидные.""" + """ (https://moscowzoo.ru/upload/iblock/d84/d8459324eabfdf192ac0d61e80f6b3bd.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Четырехцветной актимии став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')



    elif message.text == 'Павлиноглазка атлас':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Одна из крупнейших бабочек в мире, размах её крыльев может достигать 25 - 28 см. 
Крылья этой ночной бабочки окрашены в разные оттенки коричневого, ярко-красного, 
жёлтого и розового цветов и имеют по одному прозрачному «окошку» треугольной формы. 
Самка немного крупнее, её усики более короткие и узкие, чем у самца. Гусеницы последнего возраста зеленоватого цвета, 
с массивными светло-голубыми отростками по всему телу, покрыты белым восковым налётом, достигают длины 10 см. 
Куколка в плотном серовато-коричневом коконе.    """ + """ (https://moscowzoo.ru/upload/iblock/995/99568d30bc5d4526a16dd7eaf51743a7.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Павлиноглазка атлас став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')


    elif message.text == 'Совинная бабочка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Стать опекуном')
        btn2 = types.KeyboardButton('Hi, People!')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, """ Крупная и очень эффектная бабочка. В размахе крыльев достигает 130 см, иногда 150 см. 
Окраска верхней стороны крыльев тёмная с глубоким сине-фиолетовым отливом. Нижняя сторона крыльев со сложным рисунком, 
на задних крыльях имеется большой глазок, напоминающий глаз совы. Гусеницы достигают длины 13 см перед окукливанием. 
Массивная куколка прикрепляется к веткам или листьям растений.
Распространение
Тропические леса и банановые плантации Центральной и Южной Америки.  """ + """ (https://moscowzoo.ru/upload/iblock/af2/af26177f05cb7fdb9deced5817854314.jpg ).
Это Ваше Тотемное животное.
Вы можите помочь Совинной бабочке став ее опекуном, находящимся в Московском зоопарке.
ПРОСТО НАЖМИ НА КНОПОЧКУ: СТАТЬ ОПЕКУНОМ! """, parse_mode='Markdown', reply_markup=markup)

    elif message.text == 'Стать опекуном':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn1 = types.KeyboardButton(' ?')
        # markup.add(btn1)
        bot.send_message(message.from_user.id, 'Благодарим Вас за то что Вы остались не равнодушны к братьям нашим меньшим! Для более подробной информации и связи с нашим менеджером пройдите по' + '[ссылке](https://moscowzoo.ru/my-zoo/become-a-guardian/)', parse_mode='Markdown')









bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
