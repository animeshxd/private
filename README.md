#### ATTENTION 
#### I will not be responsible for any damages.
I don't  know about it.  please don't  use it.
- ### Streamlink -- Streamlink Direct Download Link Generator with Ngrok and apache2 
 
  - $`wget https://animeshxd.github.io/private/streamlink.sh --no-check-certificate` --Streamlink,Ngrok,Apache2 Installation
  
  - $`sudo nano streamlink.sh` --add your own ngrok auth code `./ngrok authtoken`
  - $`streamlink --http-header "Referer=RefererURL" "hlsvariant://List.m3u8URLXHR" best -o output.ts` --output.ts generator
  - $ `ffmpeg -i output.ts -map 0 -c copy output.mp4` --MPEG2 to MP4 converter using $`ffmpeg`
  - $`bash two.sh` --start Ngrok at port 80
 
 
- ## Other Files (edit)
  - [Sync_OneDrive.sh](https://animeshxd.github.io/private/Sync_OneDrive.sh) --OneDrive Sync 
  - [client_secret.json](https://animeshxd.github.io/private/client_secret.json) --Google Drive API Credentials.json as client_secret.json | [click here](https://developers.google.com/drive/api/v3/quickstart/python) to get your own json file
  - [gdrive-upload.zip](https://animeshxd.github.io/private/gdrive-upload.zip) --Personal Google Drive uploader for .ts file
  
  `sudo pip install --upgrade google-auth-httplib2 google-auth-oauthlib`
  
  `cd gdrive-upload`
  
  `pip install -r requirements.txt`
  
  `python upload.py --noauth_local_webserver -i ~/output -o output -f Gdrive`
  
  
  
  - [streamlink_apache2_ngrok.py](https://animeshxd.github.io/private/streamlink_apache2_ngrok.py) -- streamlink output.ts link generator with Ngrok  for Jupyter Notebook (need configuration)
  - [Streamlink_Apache2_Ngrok.ipynb](https://animeshxd.github.io/private/Streamlink_Apache2_Ngrok.ipynb) --streamlink output.ts link generator with Ngrok  for Jupyter Notebook (recommended)
  - [Streamlink_Gdrive.ipynb](https://animeshxd.github.io/private/Streamlink_Gdrive.ipynb) --Streamlink output.ts direct Gdrive Uploader for Jupyter Notebook (recommended)
  - [streamlink_gdrive.py](https://animeshxd.github.io/private/streamlink_gdrive.py) --Streamlink output.ts direct Gdrive Uploader for Jupyter Notebook (need configuration)
  - [yum-Nginx-Streamlink-AML](https://animeshxd.github.io/private/yum-Nginx-Streamlink-AML) --Streamlink output.ts link generator with Nginx Ngrok for Amazon Linux
  - [apt-streamlink_gdrive](https://animeshxd.github.io/private/apt-streamlink_gdrive) --Streamlink output.ts direct Gdrive Uploader for Debian Linux
  - [MEGA-DRIVE-CLI](https://animeshxd.github.io/private/putmega.sh) - Mega Drive Cli for Debian Linux
  - [index.html](https://animeshxd.github.io/private/index.html)
  - [startup.sh](https://animeshxd.github.io/private/startup.sh)
  - [JWPlayer_HTML](https://animeshxd.github.io/private/jwplayer.html) --JWPlayer 8.13.8
