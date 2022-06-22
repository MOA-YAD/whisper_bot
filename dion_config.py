# Copyright (C) 2022 @SeorangDion for WhisperBot repo
# FROM WhisperBot <https://github.com/SeorangDion/WhisperBot>
# t.me/DionProjects & t.me/DionSupport
# Don't remove this credits!

import os

# Config Vars
DIONAPI_HASH = "4d3f4ff02426200734b5e39ad8ae1083"
DIONAPI_KEY = 10480263
DIONBOT_NAME = os.environ.get("BOT_NAME", None) # Your bot name, example: Dion Bot
BOT_USERNAME = os.environ.get("BOT_USERNAME", None) # Your bot username with (@), example: @WhisperXRobot
DION_TOKEN = os.environ.get("TOKEN", None) # Your token bot, get one from t.me/botfather

# Config Text

HELP_TEXT = f"**• طريقة استعمال بوت {DIONBOT_NAME}:**\n\nاضغط الزر في الاسفل أو\n\nاكتب __{BOT_USERNAME} همسه <يوزر المرسل له> | <النص>__\nمثال: `{BOT_USERNAME} همسه @MOA_YAD | مرحبا!`"

