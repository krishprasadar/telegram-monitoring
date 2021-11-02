# telegram-monitoring

1) [Register app](https://my.telegram.org/apps) on teelgram here.
2) Install python3
3) Install telethon and playsound using pip3
4) Enter your creds in the creds.txt
5) Run "python3 iw.py 100 False 5" on terminal
6) The 100 means a unique identifier for your session name, keep changing whenever you want to create a new session.
7) False means that the sound alert will not contain high pitch sounds, Use True if you want (helpful during night). Check sound0 to sound2 mp3 files already there.
8) 5 means the max iteration the sound is played before it stops
9) <b>How script works is that whenever some one posts a picture it sounds an alarm.</b>
10) You can press enter to stop playing sound and it will not set of an alarm for the coming 30 mins.
11) You can also quit the script and restart it again on a terminal so it resets.

Note: the first time you login a session needs to be created which lasts for some 8 hrs i guess. Telegram has a 2 factor auth. But session is saved so you can quit script and login again without doing 2 factor.
Also since this process is running on terminal and system does't sleep I played a [countdown time](https://www.youtube.com/watch?v=xmGaAjeqaBQ) on the browser, which wouldn't make the system go to sleep.
