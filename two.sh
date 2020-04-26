sudo mv output.ts /var/www/html/
cd /var/www/html/
sudo rm index.html
sudo curl -o index.html https://animeshxd.github.io/private/index.html
cd
./ngrok http 80
