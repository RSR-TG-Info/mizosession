import asyncio
from pyrogram import Client

async def main():
    API_ID = int(input("Enter API ID: "))
    API_HASH = input("Enter API HASH: ")
    
    app = Client(name="test", api_id=API_ID, api_hash=API_HASH, in_memory=True)
    await app.start()
    session_string = await app.export_session_string()
    print(session_string)
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
