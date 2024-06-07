from pyrogram import Client, filters
import random
from AarohiX import app

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "نـسـبـة الـحـب اقـل مـن 30٪ دا بـتـاع نـسـوان ومـش بـيـحـبـك 😂💔.",
            "نـسـبـة الـحـب اقل مـن 30٪ شـوفـي حـد يـحـبـك غـيـرو😂💔..",
            "نـسـبـة الـحـب اقـل مـن 30٪ لـي يـاعـم دي الـبـت وتـڪـة حـتـى😂💔.."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "نـسـبـة الـحـب من 30٪ لـ 70٪ بـيـحبـك نـص نـص😂♥.",
            "نـسـبـة الـحـب من 30٪ لـ 70٪ هـاتـيـلـو واد عـشـان يـحـبـك اكـتـر😂♥..",
            "نـسـبـة الـحـب من 30٪ لـ 70٪ شـڪـلـو بـيـلعب بـ ديـلـو مـن وراڪـي😂♥.."
        ])
    else:
        return random.choice([
            "نـسـبـة الـحـب من 70٪ لـ 100٪ الـواد بـيـمـوت فـيـڪـي😂♥.!",
            "نـسـبـة الـحـب من 70٪ لـ 100٪ الـحـب ولـع فـ الـدرة يـ سـعـديـة😂♥.",
            "نـسـبـة الـحـب من 70٪ لـ 100٪ مـش هـنـفـرح بـيـڪـو ولا اي يـولاد😂♥.!"
        ])
        
@app.on_message(filters.command("حب", prefixes=""))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{name1}💕 + {name2}💕 = {love_percentage}%\n\n{love_message}"
    else:
        response = "حط اسمين بعد حب."
    app.send_message(message.chat.id, response)
