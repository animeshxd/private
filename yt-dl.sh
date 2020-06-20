GREEN='\033[0;32m'
NC='\033[0;97m'
echo "Enter the media URL of the file you want to download"
read link

youtube-dl -f mp4  --all-subs --yes-playlist --geo-bypass $link