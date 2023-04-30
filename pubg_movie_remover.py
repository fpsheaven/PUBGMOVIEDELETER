import os
import time
import webbrowser
import shutil
print ("Welcome to PUBG MOVIE remover. Follow the steps below.")
if os.path.exists("C:\movie_remover") == 0:
    os.mkdir("C:\movie_remover")
else:
    pass
os.chdir("C:\movie_remover")
txtpath="C:\movie_remover\path.txt"
if os.path.exists(r"C:\Program Files (x86)\Steam\steamapps\common\PUBG\TslGame\Content\Movies"):
    print ("Removing movie files from PUBG folder.")
    shutil.rmtree(r"C:\Program Files (x86)\Steam\steamapps\common\PUBG\TslGame\Content\Movies")
    time.sleep(2) # Sleep for 3 seconds
    print ("MOVIES REMOVED.Follow @FREQUENCYCS on twitter for cool WINDOWS FPS optimizations :) ")
    webbrowser.open_new_tab("https://twitter.com/fREQUENCYCS")

elif os.path.exists(txtpath):
    f = open("path.txt", "r")
    path2=f.readline()
    f.close()
    shutil.rmtree(path2)
    
else:
    path=input("Cant find PUBG.If have pubg installed on an other drive,paste the movie dir here ")
    f = open("path.txt", "w")
    f.write(path)
    f.close()
    shutil.rmtree(path)
    
    
