import textwrap

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler


from bot import dispatcher

def extrahelp(update, context):
    help_string = '''
  ✙ 📛 *𝐄𝐱𝐭𝐫𝐚* 📛 *:*
 ➻ `/song`*:* Get song from youtube
 ➻ `/tgm`*:* Upload file to telegraph
 ➻ `/tgt`*:* Upload text to telegraph
 ➻ `/whois`*:* get info from user
 ➻ `/tts`*:* Convert text to voice
 ➻ `/tl`*:* Use /tl [LANGUAGE_CODE]
 ➻ `/paste`*:* Paste text to pasty
 '''
    update.effective_message.reply_photo("https://telegra.ph/file/5682c52bcc318954ab77f.jpg", help_string, parse_mode=ParseMode.MARKDOWN)


MENUEXTRA_HANDLER = CommandHandler("menuextra", extrahelp)

dispatcher.add_handler(MENUEXTRA_HANDLER)
