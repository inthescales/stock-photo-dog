python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
crontab -l > tmp
echo "*/2 * * * * bash /var/www/bots/stock-photo-dog/scripts/run.sh" >> tmp
crontab tmp
rm tmp
