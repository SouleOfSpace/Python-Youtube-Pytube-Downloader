import pytube

def download1040(tubeObject):
    '''Скачиваем видео в качесвтве 1040'''
    nameAudio = tubeObject.title + ' audio'
    nameVideo = tubeObject.title + ' video'

    videoObject = tubeObject.streams.filter(mime_type='video/mp4', res='1080p').first()
    audioObject = tubeObject.streams.filter(mime_type='audio/mp4', only_audio=True).first()

    videoObject.download(filename=nameVideo)
    audioObject.download(filename=nameAudio)

def downloadNot1040(tube_object, res='720', path=None):
    '''Скачиваем видео в качесвтве 240 - 720'''
    filename = tube_object.title + res

    streams = tube_object.streams.filter(mime_type='video/mp4', res=res+'p').first()
    streams.download(filename=filename, output_path=path)

def getTubeObject(url):
    '''Возвращаем ютуб объект по его URL'''
    return pytube.YouTube(url)

def getTitleMediaFile(url, res):
    return getTubeObject(url).title + res

def getSizeTubeObject(url, res):
    '''Возвращаем размер медиафайла в мегабайтах'''
    size_in_bite = getTubeObject(url).streams.filter(mime_type='video/mp4', res=res+'p').first().filesize
    size_in_mega_bite = size_in_bite / 1024**2
    return size_in_mega_bite


def main(url=None, res=None, path=None):
    '''Основная функция'''
    tube_object = getTubeObject(url)
    if(res == '240' or res == '360' or res == '480' or res == '720'):
        return downloadNot1040(tube_object, res=res, path=path)


