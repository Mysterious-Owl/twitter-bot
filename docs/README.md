# TWITTER BOT

This is a twitter bot, it will like and retweet your tweet, containing some keyword and will print the url of tweet.
You can also use it to control GPIO pins of Raspberry Pi([as I did](https://youtu.be/962BUCFqvDA)) and twitter controlled home lights.
<br>
Here I used the twython library to use Twitter API, this library can be used to all the things mentioned in twitter API document. 

## Code
To use with Raspberry Pi and control GPIO use [rpicode.py](https://github.com/Mysterious-Owl/twitter-bot/blob/master/rpicode.py) and to use directly on desktop(no GPIO) use [code.py](https://github.com/Mysterious-Owl/twitter-bot/blob/master/code.py)

## Prerequisites

To install twython
```pip install twython```
or check [here](https://twython.readthedocs.io/en/latest/usage/install.html)
<br>
Generate your unique Twitter keys and token from [here](https://developer.twitter.com/en) by creating a [new app](https://developer.twitter.com/en/apps).

## How to run the script
Update the keys and tokens in code.
<br>
Run the python file and enter the keyword you want to track, now any new tweet will automatically liked and retweeted.
It will print the link of tweet<br>

## Video showing it controlling lights using Raspberry Pi

<div style="max-width:600px;">
<div style="position: relative;width: 100%;height: 0;padding-bottom: 56.25%;">
<iframe style="position: absolute;top: 0;left: 0;width: 100%;height: 100%;" src="https://www.youtube.com/embed/962BUCFqvDA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div></div>

## Screenshot showing the direct use of the script
![Editor view](https://github.com/Mysterious-Owl/twitter-bot/raw/master/Screenshot1.png)
![Twitter view](https://github.com/Mysterious-Owl/twitter-bot/raw/master/Screenshot2.png)
