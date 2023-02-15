import subprocess
import telegram
import time

TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "-1001735137359"
SERVER_ADDRESS = "176.36.160.82"

def ping_server():
    response = subprocess.call(['ping', '-c', '3', SERVER_ADDRESS], stdout=subprocess.DEVNULL)
    if response == 0:
        return True
    else:
        return False

def send_message(message):
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    server_status = ping_server()
    if server_status:
        send_message("Server is up!")
    else:
        downtime_start = time.time()
        send_message("Server is down!")
        while not server_status:
            time.sleep(60)
            server_status = ping_server()
        downtime_end = time.time()
        downtime = downtime_end - downtime_start
        send_message("Server is back up! Downtime lasted {} seconds".format(downtime))

if __name__ == "__main__":
    main()
