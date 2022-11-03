pip3 install -r ../requirements.txt
crontab -l > tmp
echo "*/2 * * * * sh /var/www/bots/stock-photo-dog/scripts/run.sh" >> tmp
crontab tmp
rm tmp
