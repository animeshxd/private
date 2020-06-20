GREEN='\033[0;32m'
NC='\033[0;97m'
echo -e "${GREEN}Enter the media URL of the file you want to download"
read link
wget $link 