from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app

@app.on_message(filters.command("معلومات الجروب", prefixes=""))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("معلومات الجروب + يوزر الجروب")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"خطا: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"➖➖➖➖➖➖➖\n"
        f"➲ اسم الجروب : {group.title} ✅\n"
        f"➲ ايدي الجروب : {group.id}\n"
        f"➲ عدد الاعضاء : {total_members}\n"
        f"➲ الوصف : {group_description or 'N/A'}\n"
        f"➲ يوزر الجروب : @{group_username}\n"
       
        f"➖➖➖➖➖➖➖"
    )
    
    await message.reply(response_text)

@app.on_message(filters.command("ايدي المجموعه", prefixes=""))
def group_status(client, message):
    chat = message.chat
    status_text = f"ايدي الجروب: {chat.id}\n" \
                  f"اسم الجروب: {chat.title}\n" \
                  f"نوع الجروب: {chat.type}\n"
                  
    if chat.username:
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)
