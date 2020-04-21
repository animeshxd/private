sudo cp output.ts /var/www/html/
cd /var/www/html/
sudo rm index.html
curl -o index.html https://animeshxd.github.io/private/index.html
cd
./ngrok http 80
