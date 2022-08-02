import webbrowser
import sys
import os

#open_new crucial URLS

factal_homepage = "https://www.factal.com/"
gmaps = "https://www.google.ca/maps"
factal_radar = "https://www.factal.com/tools/radar/"
crowdtangle_ukr = "https://apps.crowdtangle.com/factalfacebook/lists/1660922"
editorial_handover = "https://docs.google.com/document/d/1jVFn408nJur3oSkP4nxKs2iIzmXcmbTpVzJ9WNOezzw/edit"
twitter_lists = "https://docs.google.com/spreadsheets/d/1B6D7sxfu8XC4uS5oGhnR6bpOdB4YEA7v2m670-GWiNY/edit#gid=0"
news_tickers = "https://docs.google.com/spreadsheets/d/1BB9AnLtcIaWzSDUZ8QCCQrehq-a6O2daF0pePYjEQYs/edit#gid=0"
RIA = "https://ria.ru/"
gmail = "gmail.com"
ru_list =  "https://twitter.com/i/lists/1033474498656272384"
ukr_list = "https://twitter.com/i/lists/1045724714599993345"


webbrowser.open_new(factal_homepage)
webbrowser.open_new(gmaps)
webbrowser.open_new(factal_radar)
webbrowser.open_new(crowdtangle_ukr)
webbrowser.open_new(editorial_handover)
webbrowser.open_new(twitter_lists)
webbrowser.open_new(news_tickers)
webbrowser.open_new(RIA)
webbrowser.open_new(gmail)
webbrowser.open_new(ru_list)
webbrowser.open_new(ukr_list)

os.system("open /Applications/Telegram.app")

#Easy Pseudocode:
#1. store crucial URLS in strings
#2. take regions as a command line argument
#3. case statement if there is an argument
#4. open the tabs, last one should be different lists

#Harder Pseudocode:
#1. Parse CSV file
#2. Store Twitter list URLs in Hash/Dictionary
#3. take countries as arguments after regions
    #a. if arg is not in region list, check country hash
#4. pull URL from hash and convert it to string, store in array, loop array and open all of them




