# Copyright (C) 2022 GNU GENERAL PUBLIC LICENCE
#
# Licensed under the GNU GENERAL PUBLIC LICENCE, Version 3 (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2022 github.com/SeorangDion for WhisperBot repo
# FROM WhisperBot <https://github.com/SeorangDion/WhisperBot>
# t.me/DionProjects & t.me/DionSupport
# Don't remove this credits!

import logging

from telethon import events
from telethon import TelegramClient, Button
from telethon.tl.functions.users import GetFullUserRequest as us
from dion_config import *


logging.basicConfig(level=logging.INFO)


dion = TelegramClient(
        "whisper",
        api_id=DIONAPI_KEY,
        api_hash=DIONAPI_HASH
        ).start(
                bot_token=DION_TOKEN
                )
db = {}

@dion.on(events.NewMessage(pattern="^[!?/]start$"))
async def stsrt(event):
    await event.reply(
            START_TEXT)


@dion.on(events.NewMessage(pattern="^[!?/]help$"))
async def helep(event):
    await event.reply(
            HELP_TEXT,
            buttons=[
                [Button.switch_inline("Go Inline", query="همسه")]
                ]
            )


@dion.on(events.NewMessage(pattern="^[!?/]repo$"))
async def repos(event):
    await event.reply(
            REPO_TEXT,
            buttons=[
                [Button.url("Click Here", "https://telegram.dog/XTZ_HerokuBot?start=U2VvcmFuZ0Rpb24vV2hpc3BlckJvdCBkaW9u")]
                ]
            )


@dion.on(events.InlineQuery())
async def die(event):
    if len(event.text) != 0:
        return
    me = (await dion.get_me()).username

@dion.on(events.InlineQuery(pattern="همسه"))
async def inline(event):
    me = (await dion.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        user, msg = inp.split("|")
    except IndexError:
        await event.answer(
                [],
                switch_pm=f"@{me} [UserID]|[Message]",
                switch_pm_param="start"
                )
    except ValueError:
        await event.answer(
                [],
                switch_pm=f"Give a message too!",
                switch_pm_param="start"
                )
    try:
        ui = await dion(us(user))
    except BaseException:
        await event.answer(
                [],
                switch_pm="Invalid User ID/Username",
                switch_pm_param="start"
                )
        return
    db.update({"user_id": ui.user.id, "msg": msg, "gideon": event.sender.id})
    dion_text = f"""
A Whisper Has Been Sent To [{ui.user.first_name}](tg://user?id={ui.user.id})!
Click The Below Button To See The Message!\n
**Note:** __Only {ui.user.first_name} can open this!__
    """
    deon = event.builder.article(
            title="Send your secret message!",
            description=f"Powered by {DIONBOT_NAME}",
            url="https://t.me/DionProjects",
            text=dion_text,
            buttons=[
                [Button.inline(" Show Message 🔓 ", data="همسه")]
                ]
            )
    await event.answer(
            [deon],
            switch_pm="Yahoo! A secret message.",
            switch_pm_param="start"
            )


@dion.on(events.CallbackQuery(data="همسه"))
async def ws(event):
    user = int(db["user_id"])
    xflzu = [int(db["gideon"])]
    xflzu.append(user)
    if event.sender.id not in xflzu:
        await event.answer("🔐 This message is not for you ningga!", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "Oops!\nIt's looks like message got deleted from my server!", alert=True)
        return
    await event.answer(msg, alert=True)


dion_txt = 'By github.com/SeorangDion | t.me/Xflzu\n'
dion_txt += 'Any questions? Say it at t.me/DionSupport\n'
dion_txt += f'{DIONBOT_NAME} started! Developed and Maintaned by Dion\n'
print(dion_txt)
dion.run_until_disconnected()
