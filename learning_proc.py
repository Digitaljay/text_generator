import glob
import re
import codecs
import shelve

# Получаем пути до всех книг/текстов
pathes = glob.glob("*.txt")
for path in pathes:
    print(path)
    text = ''

    # Открываем файл модели
    with shelve.open("models/model") as states:
        # Проходимся по всем книгам
        with codecs.open(path, 'r', encoding='windows-1251') as text_file:
            for line in text_file:
                # Избавляемся от синтаксиса
                text += re.sub("[!?]", ".",
                               re.sub("[^абвгдеёжзийклмнопрстуфхцчшщъыьэюя .!?]", '', line.strip().lower())) + " "
            # Разбиваем весь текст на предложения
            text = text.split(".")
        # Из каждого предложения вытаскиваем биграммы
        for sentence_monolit in text:
            sentence = sentence_monolit.split()
            lenna = len(sentence)
            for word in range(0, lenna - 1):
                if sentence[word] not in states:
                    states[sentence[word]] = []
                dicta = states[sentence[word]]
                states[sentence[word]] = dicta + [sentence[word + 1]]
