import telegram_send
from datetime import datetime
def sendTelegram():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    dt_string = now.strftime("%d/%m/%Y")
    telegram_send.send(messages=["Motion detected in your house!\n\nDate :"+dt_string+"\n"+"Time :"+current_time+"\n\nTake action immediately!"])