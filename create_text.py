# -*- coding: windows-1251 -*-
import shelve
import random

random.seed(42)
most_common = ["и", "в", "не", "он", "на", "я", "тот", "быть", "с", "весь", "это", "как", "она", "по", "но", "они", "к",
               "у", "ты", "из", "мы", "за", "вы", "так", "от", "сказать", "этот", "человек", "о", "один", "такой",
               "только", "свое", "когда", "уже", "для", "вот", "кто", "знать", "мой", "до", "нет", "самый", "ни",
               "стать", "большой", "даже", "другой", "наш", "свой"]


def create_text(pref="", path="models/model", text_lenn=100):
    last_word = ""
    contin = ''
    if pref == "" or not pref[-1].isalpha():
        last_word = random.choice(most_common)
        last_word = last_word[0].upper() + last_word[1:]
        contin += " " + last_word
    else:
        last_word = pref.split(" ")[-1]

    words = 0
    with shelve.open(path) as states:
        if last_word.lower() not in states:
            contin += ". "
            last_word = random.choice(most_common)
            last_word = last_word[0].upper() + last_word[1:]
            contin += last_word
            words += 1
        while words < text_lenn:
            sentence_lenn = random.randrange(6, 10)
            words_in_sent = 0
            if last_word.lower() not in states:
                last_word = random.choice(most_common)
                last_word = last_word[0].upper() + last_word[1:]
                contin += last_word
                words += 1
                words_in_sent += 1
            while words_in_sent < sentence_lenn and last_word.lower() in states:
                nexta = random.choice(states[last_word.lower()])
                contin += " " + nexta
                last_word = nexta
                words_in_sent += 1
                words += 1
            contin += ". "
            last_word = ""

    return pref + contin


result = create_text("Как ты поживаешь? Скоро лето...")
print(result)
