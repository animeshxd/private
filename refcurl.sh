GREEN='\033[0;32m'
NC='\033[0;97m'
echo -e "${GREEN} Enter Folder Name (none to select current)"
read Folder 
mkdir $Folder
echo -e "${GREEN}Enter the media URL (https if available) of the file you want to download"
read link
echo "give output file name:"

read output
curl $link -H 'Referer: ' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' --compressed -o $Folder/$output.mp4

