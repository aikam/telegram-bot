{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import random\
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes\
from telegram import Update\
import os\
\
# \uc0\u1058 \u1088 \u1080 \u1075 \u1075 \u1077 \u1088 \u1099  \u1080  \u1086 \u1090 \u1074 \u1077 \u1090 \u1099 \
TRIGGERS = \{\
    "\uc0\u1087 \u1088 \u1080 \u1074 \u1077 \u1090 ": ["\u1047 \u1076 \u1072 \u1088 \u1086 \u1074 \u1072 !", "\u1055 \u1088 \u1080 \u1074 \u1077 \u1090 \u1080 \u1082 !", "\u1049 \u1086 \u1091 !", "\u1044 \u1086 \u1073 \u1088 \u1099 \u1081  \u1076 \u1077 \u1085 \u1100 !"],\
    "\uc0\u1073 \u1086 \u1090 ": ["\u1071  \u1090 \u1091 \u1090 !", "\u1063 \u1090 \u1086  \u1089 \u1083 \u1091 \u1095 \u1080 \u1083 \u1086 \u1089 \u1100 ?", "\u1043 \u1086 \u1090 \u1086 \u1074  \u1086 \u1090 \u1074 \u1077 \u1090 \u1080 \u1090 \u1100 ."],\
    "\uc0\u1072 \u1074 \u1080 \u1090 \u1086 ": ["\u1040 \u1074 \u1080 \u1090 \u1086  \'97 \u1089 \u1080 \u1083 \u1072 !", "\u1041 \u1099 \u1083  \u1090 \u1072 \u1084  \'97 \u1079 \u1085 \u1072 \u1102 ."]\
\}\
\
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    message = update.message.text.lower()\
\
    for word, replies in TRIGGERS.items():\
        if word in message:\
            await update.message.reply_text(random.choice(replies))\
            break\
\
if __name__ == "__main__":\
    TOKEN = os.environ.get("BOT_TOKEN")\
    app = ApplicationBuilder().token(TOKEN).build()\
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), respond))\
    print("\uc0\u1041 \u1086 \u1090  \u1079 \u1072 \u1087 \u1091 \u1097 \u1077 \u1085 ...")\
    app.run_polling()\
}