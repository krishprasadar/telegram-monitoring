from telethon import TelegramClient, events, sync
from playsound import playsound
import multiprocessing
import threading
import time
import webbrowser
import sys

dic_key = {}
with open('creds.txt') as f:
    for line in f:
        vals = line.split('=')
        dic_key[vals[0]] = vals[1].replace("\n","")
print (dic_key)
api_id = dic_key["api_id"]
api_hash = dic_key["api_hash"]
phone = dic_key["phone"]
group = 'H1B/H4 Visa Dropbox slots( No Questions only slot availability messages)'
test_group = 'Test'
session_name= 'gurleendhodyiw'
session_counter = 3
second_sound = True
arg_iteration = 5

if len(sys.argv) is not None and len(sys.argv) >= 2:
    session_name = session_name + sys.argv[1]
else:
    session_name += session_counter

if len(sys.argv) is not None and len(sys.argv) >= 3:
    second_sound = sys.argv[2].lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

if len(sys.argv) is not None and len(sys.argv) >= 4:
    arg_iteration = int(sys.argv[-1])

print (session_name, second_sound, arg_iteration)

client = TelegramClient(session_name, api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

print(client.get_me().stringify())

alreadyPlaying = False
class Threading(object):

    def __init__(self):
        global alreadyPlaying
        self.loop = True
        self.iteration = 0
        self.open = False
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        if not alreadyPlaying:                         # Daemonize thread
            thread.start()                                  # Start the execution

    def run(self):
        global alreadyPlaying
        global second_sound
        global arg_iteration

        alreadyPlaying = True
        while alreadyPlaying and self.loop and self.iteration < arg_iteration:
            for sound in ["sound0.mp3", "sound2.mp3"]:
                if alreadyPlaying and self.loop:
                    if sound == "sound2.mp3":
                        if second_sound:
                            playsound(sound)
                    else:
                        playsound(sound)
            self.iteration += 1
        self.stop()

    def stop(self):
        global alreadyPlaying
        alreadyPlaying = False
        self.loop = False
        if not self.open:
            # webbrowser.open_new('https://cgifederal.secure.force.com/')
            self.open = True

lastTimeAlert = 0
@client.on(events.NewMessage(chats=group))
async def newMessageListener(event):
    global lastTimeAlert
    global alreadyPlaying
    msg = event.message
    # print (msg)
    if msg.photo:
        print ("********************* Potential SLOT *********************")
        if lastTimeAlert + 1800 < time.time() and not alreadyPlaying:
            tt = Threading()
            string = input("Press Enter to ack and stop alert for next half hour or press \"s\" to skip alert.\n")
            print (string)
            if "s" not in string:
                lastTimeAlert = time.time()
            tt.stop()

with client:
    client.run_until_disconnected()
