import requests
import sys

argv = sys.argv
if len(argv) > 1:
    BOT_MESSAGE = "Đã chạy xong auto testing dự án Sale Marketing Admin 222.255.217.137:24087/ "
else:
    BOT_MESSAGE = "Đang thực hiện testing tự động dự án Sale Marketing Admin "

BOT_CHAT_ID = '-408028287'
token = '1312791919:AAGw-TDNSXzgbff6Vd7sPB9bgXHcLUTG2MM'
url = f'https://api.telegram.org/bot{token}/sendMessage'

data = {
    'chat_id': BOT_CHAT_ID,
    'text': BOT_MESSAGE
}
requests.post(url, data)
