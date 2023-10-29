from pytube import YouTube

def Download(link,name):
    youtubeObject=YouTube(link)
    youtubeObject=youtubeObject.streams.get_highest_resolution()
    try:
       video= youtubeObject.filter(res="144p").first().download("c:/Users/hp/Desktop/cltrH2/videoDownload/videos",name) 
    except:
        return False,""
    return True, video
    
