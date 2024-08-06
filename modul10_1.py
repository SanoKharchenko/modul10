from threading import Thread
from datetime import datetime
from time import sleep


def wite_words(word_count, file_name):
    with open(file_name,'w') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
    sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start1 = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(time_res1)
time_start2 = datetime.now()
ww5 = Thread(target=wite_words, args=(10, "example5.txt"))
ww6 = Thread(target=wite_words, args=(30, 'example6.txt'))
ww7 = Thread(target=wite_words, args=(200, "example7.txt"))
ww8 = Thread(target=wite_words, args=(100, 'example8.txt'))

ww5.start()
ww6.start()
ww7.start()
ww8.start()

ww5.join()
ww6.join()
ww7.join()
ww8.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)
