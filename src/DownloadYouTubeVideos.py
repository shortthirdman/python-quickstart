#https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/

from pytube import YouTube 
  
#where to save
SAVE_PATH = os.path.join(os.getenv('USERPROFILE'), 'Downloads') #to_do 
  
#link of the video to be downloaded 
links = open('links.txt','r') #opening the file

for i in links: 
    try: 
        #object creation using YouTube which was imported in the beginning 
        yt = YouTube(i) 
    except Exception as ex: 
        print("Connection Error", ex) #to handle exception
        print("Unexpected error: ", sys.exc_info()[0])
        raise
    except (RuntimeError, TypeError, NameError):
        pass

    #filters out all the files with "mp4" extension 
    mp4files = yt.filter('mp4') 
  
    #get the video with the extension and resolution passed in the get() function 
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 

    try: 
        #downloading the video 
        d_video.download(SAVE_PATH) 
    except: 
        print("Some Error!") 
print('Task Completed!')