GREEN='\033[0;32m'
NC='\033[0;97m'

echo -e "${GREEN} welcome"
curl -o hls-ts https://animeshxd.github.io/private/hls-ts
curl -o dl-mp4 https://animeshxd.github.io/private/dl-mp4
curl -o yt-dl https://animeshxd.github.io/private/yt-dl
echo  "Select Downloader (curl/streamlink/yt-dl)
1. streamlink
2. curl
3. youtube-dl"
read downloader
case "$downloader" in 
  1 ) bash hls-ts;;
  2 ) bash dl-mp4;;
  3 ) bash yt-dl;;
  * ) echo "invalid";;
esac
chmod +x hls-ts dl-mp4 yt-dl
