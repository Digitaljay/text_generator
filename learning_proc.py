import glob
import re
import codecs
import shelve

pathes = glob.glob("*.txt")
for path in pathes:
    print(path)
    text = ''
    with shelve.open("models/model") as states:
        with codecs.open(path, 'r', encoding='windows-1251') as text_file:
            # text_file=open(path)
            for line in text_file:
                # print(line)
                text += re.sub("[!?]", ".",
                               re.sub("[^абвгдеёжзийклмнопрстуфхцчшщъыьэюя .!?]", '', line.strip().lower())) + " "
                # text+=line
            text = text.split(".")
        for sentence_monolit in text:
            sentence = sentence_monolit.split()
            lenna = len(sentence)
            for word in range(0, lenna - 1):
                if sentence[word] not in states:
                    states[sentence[word]] = []
                dicta = states[sentence[word]]
                states[sentence[word]] = dicta + [sentence[word + 1]]
    # print(text)

with shelve.open("models/model") as states:
    print(states["раз"])
