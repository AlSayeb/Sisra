import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings.filters import command
from AarohiX import app
from config import OWNER_ID
from AarohiX.misc import SUDOERS
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX.misc import SUDOERS
import sys
from os import getenv

OWNER_ID = getenv("6300938349")
OWNER_USER_NAME = getenv("p_n_k")
NEON = getenv("NEON")

OWNER = getenv("OWNER")

from dotenv import load_dotenv
import re


@app.on_message(command(["🛡 قسم الميوزك 🛡", "✭ رجوع"]) & SUDOERS)

async def crsourceowner(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


REPLY_MESSAGE = "**👋︙مـرحـبـا بـك عـزيـزي الـمـطـور ♥️**\n**✨︙فــي قـائـمـة التحـكـم بـالـبـوت💞**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("✭ 𝖜𝖊𝖑𝖈𝖔𝖒𝖊 𝖙𝖔 𝖘𝖔𝖚𝖗𝖈𝖊 𝖗𝖊𝖆𝖑 ✭"),
    ],
    [
        ("✭ تحكم الحساب المساعد"),
    ],
    [
        
        ("✭ قسم الجروبات"),
        ("✭ السورس"),
    ],
]


    
@app.on_message(filters.command(["✭ السورس"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ قـنـاة الـسـورس"], ["✭ مطور السورس"], ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم السورس تحكم بالازار**", reply_markup=kep)

@app.on_message(filters.command(["✭ قسم الجروبات"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ الجروبات المحظوره"], ["✭ الاحصائيات"], ["✭ حـظـر الـجـروبـات"], ["✭ رجوع"], ["✭ جـروبـاتـك النـشـطـه"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الجروبات تحكم بالازار**", reply_markup=kep)

@app.on_message(filters.command(["✭ تحكم الحساب المساعد"], "") & SUDOERS)
async def mosat(client: app, message):
    kep = ReplyKeyboardMarkup([["تغير الاسم 📝"], ["تغير البايو 🔖"], ["اضافه صوره 🖼️", "• ازاله صوره •"], ["رجوع"]],resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم المساعد تحكم بالازار**", reply_markup=kep)

@app.on_message(filters.regex("✭ قـنـاة الـسـورس"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/cbsource",
        caption=f"""• My Official Channel 🫧
• I post here Source & New Updates 🫧
• My official account Dev¹ : @GGCQD 🩷
• My official account Dev² : @GGCQO 🩵""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/cbsource"),
            ]
         ]
     )
  )
  

@app.on_message(filters.regex("✭ حـظـر الـجـروبـات"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/cbsource",
        caption=f"""نبذه سريعه عن حظر جـروب🔒❌ : هذا الامر يستخدم لحظر الجروب من التشغيل عن طريق اليوزر او الايدي🫡\nاستخدم الامر بهذا الشكل blacklistchat اضغط علي الامر لنسخ والاستخدام واتبع التعليمات🩵""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/cbsource"),
            ]
         ]
     )
  )
  
@app.on_message(filters.regex("✭ الاحصائيات"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/cbsource",
        caption=f"""نبذه سريعه عن 💡︙الاحصائيات ︙💡 : يتم استخدام هذا الامر لعرض من احصائيات البوت🫡\nاستخدم الامر بهذا الشكل `الاحصائيات` اونلاين اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/cbsource"),
            ]
         ]
     )
  )
  
@app.on_message(filters.regex("✭ الجروبات المحظوره"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/cbsource",
        caption=f"""نبذه سريعه عن قائمه الحظر❌ : يتم استخدام هذا الامر لعرض من هم المحظورين من تشغيل البوت من قبل المالك او المطورين الذي تم رفعهم🫡\nاستخدم الامر بهذا الشكل قائمه الحظر اضغط علي الامر لنسخ والاستخدام""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/cbsource"),
            ]
         ]
     )
  )    
  
@app.on_message(filters.regex("✭ جـروبـاتـك النـشـطـه"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/cbsource",
        caption=f"""نبذه سريعه عن 💡︙جـروبـاتـك النـشـطـه︙💡 : يتم استخدام هذا الامر لعرض من يقوم بتشغيل البوت الان في المحادثه الصوتية🫡\nاستخدم الامر بهذا الشكل اونلاين اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/cbsource"),
            ]
         ]
     )
  )    

@app.on_message(filters.regex("✭ مطور السورس"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/p_n_k",
        caption=f"""[﹟◟Ꭵ ᭙Ꭵᥣᥣ ᥉𝗁Ꭵꪀᥱ Ꭵꪀ Y᥆υᖇ ꪔᥱꪔ᥆ᖇY ᖴ᥆ᖇᥱ᥎ᥱᖇ ✨ . ⋆ ❘❘ ᥴ𝗁: @I_YIQ ❘❘ Ⴆᖴᖴ ႦᥱႦᥲ️ ៸៸ . ⊀ ](https://t.me/p_n_k)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/p_n_k"),
            ]
         ]
     )
  )


@app.on_callback_query(filters.regex("✭ قـفـل الـكـيـبـورد") & filters.private & SUDOERS)
async def italy(_, query: CallbackQuery):
   await callback_query.edit_message_caption(caption =f"""**♬ تــم حــذف الــڪــيــبــورد .**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⸢  𝗠𝗥 . 𝗫  ⸥", url=f"https://t.me/zzxxue "),
               ],
            ]
        ),
    )
