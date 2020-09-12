import webbrowser
import os
import os.path
from os import path
import requests

Second_loop = True
Second_loop_1 = True
main_loop = True
new = 0
retry_url = True



Folder_check = path.exists("./myAnime")
file_check = path.exists("./myAnime/existed")

while Folder_check == False:
    os.mkdir("./myAnime")
    break
while file_check == False:
    retry_url = False
    print("file checked not available")
    break

while main_loop:
    vids = "http://xkali.centralindia.cloudapp.azure.com/"

    anime = str(input('Enter Anime url: '))

    anime_name = anime.replace('http://xkali.centralindia.cloudapp.azure.com/', '')
   

    print(anime_name)
    logicforlast = False

    if anime.lower() == "exit" or anime.lower() == "q":
        break
    if anime == '':
        break

    if anime.lower() == "o" and file_check == False:
        print("We can't find any saved anime Available")
        retry_url = False
        

    if anime.lower() != "o":
        retry_url = True
        file_check = True
        logicforlast = False
        
    print(retry_url)

    if (anime.lower() == "o" or anime.lower() == "last") and file_check and retry_url:
        open3 = os.popen("cat ./myAnime/Anime_Name-last").read()
        watched_ep = os.popen("cat ./myAnime/Anime_EP-last").read()
        
        #annm = open3.replace('-',' ')
       # annm = annm.replace('episode','')
       # annm = annm.upper()
        print(f"\nOpening Episode No: {watched_ep}")
       # print(f"{vids}{open3}{watched_ep}")

        logicforlast = True
        anime_name = open3
        # print(f"loop o is working ")

        my_url = f"{vids}{open3}{watched_ep}.mp4"

        
        # webbrowser.open(f"{vids}{open3}{watched_ep}")
        # os.system(f"termux-open-url {vids}{open3}{watched_ep}")
    # else:
        # print("loop o is not working")
    #annm = anime_name.replace('-',' ')
    #annm = annm.replace('episode','')
    #annm = annm.upper()
    #print(annm)

    while Second_loop_1:
        while Second_loop:
            scrap_bool = True

            if file_check == False:
                break
            else:
                retry_url = True

            if logicforlast == False:
                ep = str(input("\nEnter Episode number: "))
                Anime_Episode = ep

            

            while logicforlast == True:
                Anime_Episode = watched_ep
                new = int(watched_ep)
                # print(f"{logicforlast} logicforladt")
                integerlogic = False
                ep = ''
                break
            logicforlast = False
            if ep.lower() == "exit" or ep.lower() == "q":
                break
            elif ep == '':
                print("")

           # file_check_1 = path.exists('./'


            elif ep.lower() == "n" or ep.lower() == "next":

                new = new + 1

                Anime_Episode = str(new)

                # open2 = f"{vids}{anime_name}{Anime_Episode}"

                my_url = f"{vids}{anime_name}{Anime_Episode}.mp4"

               # print(f"Opening Episode No. {Anime_Episode} \n {open2}")
                print(f"\nOpening  \nEpisode No. {Anime_Episode}")
                os.system(f"printf {anime_name} > ./myAnime/Anime_Name-last && printf {Anime_Episode} > ./myAnime/Anime_EP-last && touch ./myAnime/existed")

                logicforlast = False

            #   webbrowser.open(open2)
                # os.system(f"termux-open-url {open2}")

            

            elif ep.isdigit():
                
                open2 = f"{vids}{anime_name}/{anime_name}{Anime_Episode}"
                #print(f"Opening Episode No. {Anime_Episode} \n {open2} ")
                print(f"\nOpening  \nEpisode No. {Anime_Episode}")
                new = int(Anime_Episode)

                os.system(f"printf {anime_name} > ./myAnime/Anime_Name-last && printf {Anime_Episode} > ./myAnime/Anime_EP-last")

                logicforlast = False
                my_url = f"{vids}{anime_name}{Anime_Episode}.mp4"
                # webbrowser.open(open2)
                # os.system(f"termux-open-url {open2}")
            
            else:
                open2 = f"{vids}{anime_name}{Anime_Episode}"
                print(f"\nNo Episode Avaiable {Anime_Episode}")
                scrap_bool = False
        #       webbrowser.open(open2)
        #   #  os.system(f"termux-open-url {open2}")

            logicforlast = False
            connection_status = requests.get(my_url,stream=True,verify=False, timeout=10)
            if connection_status.status_code == 404:
                print('\nAnime Not Found 404 status\n')
                break
             # webbrowser.open(open2)
            # os.system(f"termux-open-url {open2}")
            print(f"webbrowser link: {my_url}")

        

              


            webbrowser.open(my_url)
            os.system(f"termux-open-url {my_url}")
            #os.system(f'echo " \n {anime_name}{Anime_Episode}\n">./myAnime/{anime_name}{Anime_Episode}-ep && printf "$(date +"%m-%d-%y") Anime Name: {anime_name}"%s"\n" ./myAnime/*-ep > ./myAnime/savelist.txt')
        break

