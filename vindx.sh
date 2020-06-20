GREEN='\033[0;32m'
NC='\033[0;97m'
echo -e "${GREEN} welcome"
rm stmli refcurl yt-dl
curl -o stmli https://animeshxd.github.io/private/stmli.sh
curl -o refcurl https://animeshxd.github.io/private/refcurl.sh
curl -o yt-dl https://animeshxd.github.io/private/yt-dl.sh
echo  "Select Downloader (curl/streamlink/yt-dl)
1. streamlink
2. curl
3. youtube-dl"
read downloader
case "$downloader" in 
  1 ) bash stmli;;
  2 ) bash refcurl;;
  3 ) bash yt-dl;;
  * ) echo "invalid";;
esac
chmod +x stmli refcurl yt-dl