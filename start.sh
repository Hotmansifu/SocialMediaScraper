#!/bin/bash
echo 'Welcome to Poc Osint Tool (Team Genesis)'
echo 'Instagram 1'
echo 'Facebook 2'
echo 'twitter 3'
echo  'Please Select An Option: '
read option
#echo hello $option
if [ "$option" = 2 ];
then
python3 fb_scrape.py
fi
if [ "$option" = 3 ];
then
python3 twitter_scraper.py
fi
if [ "$option" = 1 ];
then
cd Osintgram/
echo 'Please Provide Username: '
read username
make setup
python3 main.py $username
fi


