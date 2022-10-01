pip3 install -r ../requirements.txt
crontab -l > tmp
echo "*/30 * * * * sh /var/www/bots/lyres-dictionary/scripts/dog.sh" >> tmp
crontab tmp
rm tmp
