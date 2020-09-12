from urllib.request import urlopen, Request

from bs4 import BeautifulSoup
import json
import ast
import os
import os.path
from os import path
import requests
import sys

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

# reg_url = "shi-zhi-ge-hua-yu-yan-de-kuangxiang-shi-episode-8"

Anime_Url = input('Enter url: ')
Anime_Name = Anime_Url.replace('https://vidstreaming.io/videos/', '')
# print(Anime_Name)
Anime_Episode = 0
Anime_Start = 0
Main_Loop = True

Folder_check = path.exists("./Anime_downloader")
while Folder_check == False:
    os.mkdir("./Anime_downloader")
    break
Anime_Folder = './Anime_downloader'


while Main_Loop:
    # Anime_Episode = 1
    Anime_Episode = Anime_Episode + 1
    Anime_Name_Full = f"{Anime_Name}{Anime_Episode}"
    # print(Anime_Name_Full)
    print(f"\nDownloading Episode {Anime_Episode}")

    reg_url = f"{Anime_Url}{Anime_Episode}"
    my_request = Request(url=reg_url, headers=headers)

    html = urlopen(my_request)
    my_iframe = BeautifulSoup(html.read(), "html5lib")
    error = my_iframe.body.get_text()
    # print(error)
    if error == "404\n":
        print("No Anime Available")
        break
    vidstreaming = "http:" + str(my_iframe.iframe["src"])

    # print(vidstreaming)
    vidstreaming = vidstreaming.replace('streaming.php', 'ajax.php')
    # print(vidstreaming)

    my_request = Request(url=vidstreaming, headers=headers)
    html = urlopen(my_request)
    my_iframe = BeautifulSoup(html.read(), "html5lib")
    # print(my_iframe)
    stream_json = my_iframe.body.get_text()

    # print(stream_json)
    # print(type(stream_json))

    stream_json = json.loads(stream_json)

    # print(stream_json)

    # print(type(stream_json))

    stream_json = stream_json['source']
    stream_json = str(stream_json)
    stream_json = stream_json.replace('[', '')
    stream_json = stream_json.replace(']', '')
    # print(type(stream_json))
    stream_json = ast.literal_eval(stream_json)
    # print(stream_jsonn)

    stream_json = stream_json.get("file")

    # print(stream_json)
    Anime_download_path = f"./Anime_downloader/{Anime_Name_Full}.mp4"

    with open(Anime_download_path, "wb") as f:
        print("Downloading %s" % Anime_Name_Full)
        response = requests.get(stream_json, stream=True, allow_redirects=True)
        total_length = response.headers.get('content-length')
        print("File size: %s MB" % int(int(total_length) / (1024 * 1024)))

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            # 1000 equals to 1 MB bandwidth
            for data in response.iter_content(chunk_size=100000):
                dl += len(data)
                f.write(data)
                done = int(40 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('█' * done, ' ' * (40-done)))
                sys.stdout.flush()

    # ██████████████████████████████████████████████████
    # loop_start = True
    # a = Anime_Episode
    # b = 0
    # while loop_start:
    #   b = b + 1
    #   process = "█" * b

    #   if b == a:
    #     break
    #   print(process)

    # print(os.popen(f"wget -O ./Anime_downloader/{Anime_Name_Full}.mp4 {stream_json} ").read())

    # dnld_type_m3u8 = 'm3u8' in stream_json
    # dnld_type_mp4 = 'mp4' in stream_json

    # print(f"m3u8 = {dnld_type_m3u8}")
    # print(f"mp4 = {dnld_type_mp4}")
    # if dnld_type_m3u8 == True and dnld_type_mp4 == False:
    #   print("Downloading m3u8 ")
    #   os.system(f'curl -o  ./Anime_downloader/{Anime_Name_Full}.txt {stream_json}')

    # elif dnld_type_mp4 == True and dnld_type_m3u8 == False:
    #   print("Downloading mp4")

    #   filename = wget.download(stream_json, out=Anime_Folder)
    # else:
    #   print("contact developer")

    # break
