GREEN='\033[0;32m'
NC='\033[0;97m'
echo -e "${GREEN} Enter Folder Name (none to select current)"
read Folder 
mkdir $Folder
echo "Enter the Youtube URL"
read link
echo "give output file name:"

read output
youtube-dl -f mp4  -o $Folder/$output.mp4 --yes-playlist --geo-bypass $link