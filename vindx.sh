RED='\033[0;32m'
NC='\033[0;97m'
rm stmli.sh refcurl.sh yt-dl.sh
curl -o stmli.sh https://animeshxd.github.io/private/stmli.sh
curl -o refcurl.sh https://animeshxd.github.io/private/refcurl.sh
curl -o yt-dl.sh https://animeshxd.github.io/private/yt-dl.sh
echo -e " ${GREEN}Select Downloader (curl/streamlink/yt-dl)
1. streamlink
2. curl
3. youtube-dl"
read choice
echo -e "${NC}"
case "$downloader" in 
  1 ) bash stmli.sh;;
  2 ) bash refcurl.sh;;
  3 ) bash yt-dl.sh;;
  * ) echo "invalid";;
esac
