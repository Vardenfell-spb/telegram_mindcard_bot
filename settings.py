MESSAGE = {
    1: {'start': 'Это бот, имитирующий технику запоминания слов при помощи карточек\n'
                 'Нажмите одну из кнопок, чтобы начать, /help для инструкции или /settings для выбора изучаемых языков '
                 'и языка интерфейса 🇷🇺·🇬🇧',
        'no cards': '✔ Вы повторили все карточки!\n💰 Можете помочь боту развиваться тут:',
        'create': 'Пришлите сообщение со словом и его переводом на следующей строке',
        'translate': 'Отправьте слово для перевода\nВыбрать языки /settings',
        'delete': 'Вы точно хотите удалить карточку?',
        'default': 'Выберите необходимое действие:',
        'repeat': 'Повторение карточек, осталось: ',
        'help': ['Кнопка [Create]\n\nВы создаете карточку, чтобы запомнить слово:\n'
                 '1. Пишите новое слово в первой строке вашего сообщения\n'
                 '2. На второй строке пишется его значение, которое нужно будет вспомнить при повторении\n'
                 '3. Отправляете сообщение боту. Должно появиться уведомление о создании карточки\n\n'
                 'Если в вашем сообщении только одна строка, она будет переведена командой Translate',
                 'Кнопка [Translate]\n\nПомощник [Create]:\n1. Вы отправляете слово, которое нужно перевести\n'
                 '2. Бот присылает в ответ шаблон для создания карточки с переводом от Google translate\n\n'
                 '💾 - сохранение карточки\n↻ - поменять слова местами\n🏴‍☠ - поставить флаг языка\n\n'
                 'Поменять языки перевода можно в настройках: /settings',
                 'Кнопка [Repeat]\n\n▤ ⇒ ≣ ⇒ 20≟\n1. Бот берёт все карточки, '
                 'которые нужно повторить сегодня из сохраненных '
                 'и выдаёт их стопкой в 20 штук (можно изменить в настройках)\n'
                 '20≟ ⇔ ✔6\n2. Каждую карточку нужно повторить  три раза с одной стороны и три раза с другой\n'
                 '19≟ ⇒ ▤\n3. Когда слово повторили, бот сохраняет карточку для следующего повторения '
                 'и убирает из стопки\n'
                 '≣ ⇒ 20≟\n4. Из сегодняшних карточек в стопку добавляется новая\n\n'
                 'Интервал повторения увеличивается от одного дня в два раза при каждом '
                 'удачном повторении.\n\n Кнопки:\n✔ - нажимаете, если вы вспомнили значение карточки\n'
                 '✖ - если не можете вспомнить (в этом случае вы смотрите значение '
                 'под спойлером и придумываете ассоциации, чтобы лучше запомнить)\n'
                 '🚮 - удаление ненужной карточки\n🎵 - позволяет прослушать, как звучит слово, голосом Google '
                 'translate. Язык озвучки - тот, который вы учите, из настроек /settings',
                 'КОМАНДЫ\n\n/load_all - загружает все ваши карточки, all можно заменить на число, тогда бот пришлет '
                 'вам карточки, которые нужно повторить за это количество дней\n'
                 '/load_user_cards - показывает карточки, которые пришло время повторить на данный момент\n'
                 '/settings - Настройки бота:\n'
                 '  - количество карточек, повторяемых одновременно\n  - язык интерфейса\n'
                 '  - язык для перевода по умолчанию\n  - язык с которого переводит по умолчанию'],
        'name_change': {
            'yes': 'Теперь вас зовут ',
            'fail': 'Вы должны набрать максимальное количество очков за неделю.\nИспользуйте /stats для проверки',
            'win': '\n﹋\nВы выиграли и можете выбрать имя!\n',
            'stats': 'Используйте команду /name ВАШЕ_ИМЯ\n'
                     'Изменений имени доступно: ',
            'no one': '\nНикто ещё не получил очков',
            'stats_head': 'Лидеры недели:\n﹏',
            'stats_info': '\n﹋\nПобедитель недели получает возможность изменить ник в таблице',
        }
        },
    0: {
        'start': 'It is the bot for learning word by mind cards\nPress button for start of look /help for more',
        'no cards': '✔ You have repeated all the words!\n💰 You can help the bot grow here:',
        'create': 'Send the word and its translation on the next line',
        'translate': 'Send a word for translate\nChange langs /settings',
        'delete': 'Do you want to delete the Card?',
        'default': 'Choose what you need:',
        'repeat': 'Repeating of cards, left: ',
        'help': ['Button [Create]\n\nYou create a card to memorize a word\n'
                 'On one side is the word, on the other side is its meaning\n'
                 'Button [Translate]\n\nAn assistant to Create. You write the word, '
                 'the bot sends in response a template for creating a card with translation '
                 'from Google translate\n'
                 'Button [Repeat]\n\nThe bot takes all the cards you need to repeat today, '
                 'and gives them a stack of 20 pieces, '
                 'where each card must be repeated three times on one side and three times on the other\n'
                 'When the word is repeated, the bot removes the card from the stack '
                 'and adds a new one from todays cards\n'
                 'The interval for repeating cards increases from one day to twice '
                 'for each successful repetition\n'
                 '✔ button means you remember the meaning of the card, '
                 '✖ button means you can not remember '
                 '(in this case you look up the meaning under a spoiler and make up '
                 'associations to remember it better)\n'
                 'You can also delete a card if you do not need it anymore, with the 🚮 button, '
                 'and listen to how the word sounds in Google translate voice with 🎵\n'],
        'name_change': {
            'yes': 'Now your name is ',
            'fail': 'You need to get MAX week score for change your name\nUse /stats to check',
            'win': '\n﹋\nYou won and now can choose name!\n',
            'stats': 'Use /name YOUR_NICKNAME command\nNickname change available: ',
            'no one': '\nNo one get scores yet',
            'stats_head': 'Weekly leaderboard:\n﹏',
            'stats_info': '\n﹋\nWinner of week can change his leaderboard nickname',

        }
    }
}

FLAGS = {
    'ru': '🇷🇺',
    'uk': '🇺🇦',
    'en': '🇬🇧',
    'fr': '🇫🇷',
    'es': '🇪🇸',
    'it': '🇮🇹',
    'de': '🇩🇪',
    'zh-CN': '🇨🇳',
    'ja': '🇯🇵',
    'ko': '🇰🇷',
    'hy': '🇦🇲',
    'ka': '🇬🇪',
    'tr': '🇹🇷',
}
INTERFACE = {
    # English interface
    0: {
        'settings': {
            0: 'Stack',
            1: 'Interface',
            2: 'To',
            3: 'From',
            4: '🔧 SETTINGS',
            5: ['Add', 'to', 'stack'],
            'cancel': 'Cancel',
            'change_name': 'Change name',
        },
    },
    # Russian interface
    1: {
        'settings': {
            0: 'Стопка',
            1: 'Интерфейс',
            2: 'На',
            3: 'С',
            4: '🔧 НАСТРОЙКИ',
            5: ['Подкидывать', 'в', 'стопку'],
            'cancel': 'Отмена',
            'change_name': 'Сменить имя',
        },
    },
    'interface_langs': ['en', 'ru'],
    'translate_langs': ['ru', 'en', 'uk', 'fr', 'es', 'it', 'de', 'zh-CN', 'ja', 'ko', 'hy', 'ka', 'tr'],
}
