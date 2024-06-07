from AarohiX.core.userbot import assistants
from AarohiX import userbot as us, app
from pyrogram import filters
from strings.filters import command
from pyrogram.types import Message
from AarohiX.misc import SUDOERS
from config import BANNED_USERS, OWNER_ID


@app.on_message(command(["اضافه صوره 🖼️", "وضع صوره"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("استنا بغيير الصوره...")
        img = await message.reply_to_message.download()
        if 1 in assistants:
           ubot = us.one
        try:
            await ubot.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» {ubot.me.mention} تم غيرتها يقلبي."
            )
        except:
            return await fuk.edit_text("تم تغيير صوره المساعد بنجاح.")
    else:
        await message.reply_text(
            "ريب علي الصوره ال انت عاوزها.."
        )


@app.on_message(command(["• ازاله صوره •", "حذف الصوره"]) & filters.user(OWNER_ID))
async def set_pfp(_, message: Message):
    try:
        if 1 in assistants:
           ubot = us.one
        pfp = [p async for p in ubot.get_chat_photos("me")]
        await ubot.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text( "تم حذف صوره المساعد بنجاح" )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("فشل في ازاله الصوره.")


@app.on_message(command(["تغير البايو 🔖", "وضع بايو"]) & filters.user(OWNER_ID))
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            if 1 in assistants:
               ubot = us.one
            await ubot.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ubot.me.mention} تم تغيير البايو."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        if 1 in assistants:
           ubot = us.one
        await ubot.update_profile(bio=newbio)
        return await message.reply_text(f"» {ubot.me.mention} تم تغيير البايو بنجاح")
    else:
        return await message.reply_text(
            "اعمل ريب علي البايو ال عاوز تحطها."
        )


@app.on_message(command(["تغير الاسم 📝", "وضع اسم"]) & filters.user(OWNER_ID))
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            if 1 in assistants:
               ubot = us.one
            await ubot.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ubot.me.mention} تم تغيير الاسم بنجاح."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        if 1 in assistants:
           ubot = us.one
        await ubot.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ubot.me.mention} تم تغيير الاسم")
    else:
        return await message.reply_text(
            "اعمل ريب علي الاسم ال انت عاوز تحطه"
        )
        
