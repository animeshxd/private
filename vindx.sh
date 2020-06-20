RED='\033[0;32m'
NC='\033[0;97m'
echo -e "${GREEN} Enter Folder Name (none to select current)"
read Folder 
mkdir $Folder

rm stml.sh refcurl.sh yt-dl.sh
curl -o $Folder/stmli.sh https://animeshxd.github.io/private/stmli.sh
curl -o $Folder/refcurl.sh https://animeshxd.github.io/private/refcurl.sh
curl -o $Folder/yt-dl.sh https://animeshxd.github.io/private/yt-dl.sh


echo -e " ${GREEN}Select Downloader  (curl/streamlink/yt-dl)
1. streamlink
2. curl
3. youtube-dl"
read downloader
echo -e "${NC}"
case "$downloader" in 
  1 ) bash $Folder/stmli.sh;;
  2 ) bash $Folder/refcurl.sh;;
  3 ) bash $Folder/yt-dl.sh;;
  * ) echo "invalid";;
esac
