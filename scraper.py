from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os
import sys
import configparser
import csv
import time


cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(" Please run python3 setup,py first and follow along readme,txt")
    sys.exit(1)

client.connect()
if not client, is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(+'Enter your Code:'))

os.system('clear')
banner()
chats = []
groups[]
chunk_size = 200

result = client(GetDialogsRequest(
    offset_date=last_date
    offset_id=0
    offset_peer=InputPeerEmpty
    limit=chunk_size
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)

    else:
        continue


print('Chose a group to scrape members:')

i = 0

for group in groups:
    print('['str(i)']' + group.title)
    i += 1

print('')

group_index = input("Enter a Number :")
target_group = groups[int(group_index)]

print("Fetching......")
time.sleep(1)


with open("members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimeter=",", lineterminator="\n")
    writer.writerow(['username', 'user id',  'access hash',
                     'name', 'group',  'group id'])

    for user in all_participants:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""

        name = (first_name + ' ' + last_name).strip()
        writer.writerow([username, user.id, user.access_hash,
                         name, target_group, title, target_group.id])

print('SCRAPED SUCCESSFULLY')
