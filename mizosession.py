from pyrogram import Client

API_ID = int(input("Enter API ID: "))
API_HASH = input("Enter API HASH: ")

app = Client(name="test", api_id=API_ID, api_hash=API_HASH, in_memory=True)
app.start()
session_string = app.export_session_string()
print(session_string)
app.stop()
