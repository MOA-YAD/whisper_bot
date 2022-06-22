# Copyright (C) 2022 GNU GENERAL PUBLIC LICENCE
#
# Licensed under the GNU GENERAL PUBLIC LICENCE, Version 3 (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2022 github.com/MOA-YAD for WhisperBot repo
# FROM WhisperBot <https://github.com/MOA-YAD/whisper_bot>
# t.me/MOA-YAD & t.me/MOA_YAD
# Don't remove this credits!

import logging

from telethon import events
from telethon import TelegramClient, Button
from telethon.tl.functions.users import GetFullUserRequest as us
from dion_config import *


logging.basicConfig(level=logging.INFO)


dion = TelegramClient(
        "",
        api_id=DIONAPI_KEY,
        api_hash=DIONAPI_HASH
        ).start(
                bot_token=DION_TOKEN
                )
db = {}

@dion.on(events.NewMessage(pattern="^[/]Whisper$"))
async def helep(event):
    await event.reply(
            HELP_TEXT,
            buttons=[
                [Button.switch_inline("ارسال همسه", query="")]
                ]
            )


@dion.on(events.InlineQuery())
async def die(event):
    if len(event.text) != 0:
        return
    me = (await dion.get_me()).username

@dion.on(events.InlineQuery(pattern=""))
async def inline(event):
    me = (await dion.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        user, msg = inp.split("|")
    except IndexError:
        await event.answer(
                [],
                switch_pm=f"@{me} [ايدي او يوزر]|[الرساله]",
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
                switch_pm="اليوزر غلط ",
                switch_pm_param="start"
                )
        return
    db.update({"user_id": ui.user.id, "msg": msg, "gideon": event.sender.id})
    dion_text = f"""
الهمسه الا [{ui.user.first_name}](tg://user?id={ui.user.id})!
اضغط على الزر علمود اتشوف الهمسه!\n
**ملاحضه:** __فقط {ui.user.first_name} يكدر يفتح الهمسه!__
    """
    deon = event.builder.article(
            title="ارسال همسه!",
            description=f"في خلل راسل المطور",
            url="https://t.me/MOA_YAD",
            text=dion_text,
            buttons=[
                [Button.inline(" اضهار الهمسه 🔓 ", data="")]
                ]
            )
    await event.answer(
            [deon],
            switch_pm="اضغط لاُرسال همسه.",
            switch_pm_param="start"
            )


@dion.on(events.CallbackQuery(data=""))
async def ws(event):
    user = int(db["user_id"])
    xflzu = [int(db["gideon"])]
    xflzu.append(user)
    if event.sender.id not in xflzu:
        await event.answer("ولي هاي الهمسه مو الك 👞!", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "Oops!\nIt's looks like message got deleted from my server!", alert=True)
        return
    await event.answer(msg, alert=True)


dion_txt = 'By github.com/moa-yad | t.me/moa-yad\n'
dion_txt += f'{DIONBOT_NAME} started! Developed and Maintaned by Dion\n'
print(dion_txt)
dion.run_until_disconnected()
