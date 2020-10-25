import os
import pytube

# file = os.stat('Python как сделать красивую программу под ПК за 10 минут 720.mp4')
# print(file.st_size / (1024**2))
# print(os.getcwd())

# tubeObject = pytube.YouTube('https://www.youtube.com/watch?v=VFBXx7O9BxU')
# fv = tubeObject.streams.first().download(filename='hh', output_path='D:\\Draft Python\\YoutubeDownloader\\media')
# # print(fv.filesize / (1024**2))
import threading

def getSizeFile(filename, path=os.getcwd()):
    path = path + '\\' + filename
    '''Возвращаем размер файла в мегабайтах'''
    return os.stat(path).st_size / 1024**2

def writer(x, event_for_wait, event_for_set):
    for i in range(10):
        event_for_wait.wait() # wait for event
        event_for_wait.clear() # clean event for future
        print(x)
        event_for_set.set() # set event for neighbor thread

# init events
e1 = threading.Event()
e2 = threading.Event()

# init threads
t1 = threading.Thread(target=writer, args=(0, e1, e2), daemon=True)
t2 = threading.Thread(target=writer, args=(1, e2, e1), daemon=True)

# start threads
t1.start()
t2.start()

e1.set() # initiate the first event

# join threads to the main thread
t1.join()
t2.join()
