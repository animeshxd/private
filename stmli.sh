GREEN='\033[0;32m'
NC='\033[0;97m'
echo "Enter the media URL of the file you want to download"
read link
echo "checking quality.."
streamlink hlsvariant://$link
echo -e " ${GREEN}Select Quality (none to select default quality)
1. best
2. worst
3. custom"
read choice
echo -e "${NC}"
case "$choice" in 
  
  1 ) quality='best';;
  2 ) quality='Worst';;
  3 ) echo "Select Quality" && read quality ;;
  * ) quality='best';;
esac

echo $quality

streamlink hlsvariant://$link $quality -o output.ts