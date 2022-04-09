import discord
import random
import asyncio
import time
import os
import io
import shutil
import schedule
import time
import datetime as dt
import itertools
from discord.ext import tasks
from random import randint

client = discord.Client(
    intents=discord.Intents.all()
)
a = 0
# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

    time_check.start()
    change_sex.start()
    
@tasks.loop(seconds=5)
async def change_sex():
    sex = itertools.cycle(["마감", "섹스", "운전", "화공", "하는 중 하는 중 하는 중 하는 중 하는 중"])
    await client.change_presence(activity=discord.Game(next(sex)))

@tasks.loop(seconds=1)
async def time_check():
    ids = [
        810490718979489845,
        772475285320237069,
    ]
    channels = [client.get_channel(id) for id in ids]  
    now = dt.datetime.now()

    if now.hour == 18 and now.minute == 0 and now.second == 0:
        for ch in channels:
            await ch.send("https://youtu.be/H04dl1te52Q")

    if now.hour == 8 and now.minute == 30 and now.second == 0:
        for ch in channels:
            await ch.send("구닌들 폰 받는시간!!")
    
    if now.hour == 12 and now.minute == 0 and now.second == 0:
        for ch in channels:
            await ch.send("구닌들 폰 내는시간ㅠㅠ")

    if now.hour == 13 and now.minute == 0 and now.second == 0:
        for ch in channels:
            await ch.send("https://media.discordapp.net/attachments/803945796151279636/958309861903458324/IMG_2999.png")

    if now.hour == 22 and now.minute == 0 and now.second == 0:
        for ch in channels:
            await ch.send("https://media.discordapp.net/attachments/803945796151279636/958309862691975198/IMG_2996.png")

channels_500x_enabled = []
a = 0
KST=dt.timezone(dt.timedelta(hours=9))
dai = dt.datetime.now(tz=KST).day

@client.event
async def on_message(message):

    global a
    global dai
    a += 1
    channel = message.channel
    
    if not dai == dt.datetime.now(tz=KST).day:
        a = 0
        dai = dt.datetime.now(tz=KST).day
    
    if a == 777:
        await channel.send('축하합니다! 당신이 방금 한 발언은 오늘의 777번째 채팅!!!!!!!!')
    
    if a == 7777:
        await channel.send('뱅 뱅 와우!!!!!!!!! 당신이 방금 한 발언은 오늘의 7777번째 채팅!!!!!!!! 홀리 씻 오마이 갓 세상에나 마상에!!!!!!!!오 와우!!!!!!!!!!!!!!!!!!!')

    if randint(1, 1000) == 1:
        await message.delete()
        await channel.send("축하합니다!" + message.author.mention + "님은 0.1% 확률에 걸렸습니다! 다음엔 조용히 얘기해주세요!!!!!")

    if message.author.bot:
        return

    if '오백배' in message.content:
        if not message.mentions:
            return

        target = message.mentions[0]
        channels_500x_enabled.append(channel)
        for i in range(500):
            if channel not in channels_500x_enabled:
                return
            await channel.send(target.mention)
            await asyncio.sleep(3)

    if 'ㅅㅂ' in message.content and channel in channels_500x_enabled:
        await channel.send('ㅈㅅ')
        channels_500x_enabled.remove(channel)
        return

TOKEN = os.getenv('BOT_TOKEN')
client.run(TOKEN)
