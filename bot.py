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

    if now.hour == 7 and now.minute == 30 and now.second == 0:
        for ch in channels:
            await ch.send("구닌들 폰 받는시간!!")
    
    if now.hour == 11 and now.minute == 0 and now.second == 0:
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
    
    if randint(10000, 20000) == 10001:
            await message.delete()
            await channel.send("축하합니다!" + message.author.mention + "님은 0.01% 확률에 걸렸습니다ㅋㅋㅋㅋㅋ 이게 걸리네 병신새낔!")

    if message.author.bot:
        return
    
    if '테스트' in message.content:
        await channel.send('이모나모노와이야')

    if '오벡배' in message.content:
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
    
    if '구론희뽑기' in message.content:
        await channel.send("구론희의 뽑기 타임!!")
        time.sleep(2.0)
        await channel.send("뭐가 나올까? 두구두구두구..")
        time.sleep(3.0)
        anser = "응가 https://media.discordapp.net/attachments/812665665437696020/1008500266347274270/FaceApp_1639364043809.jpg https://media.discordapp.net/attachments/812665665437696020/816677434866270258/Screenshot_20210303-232421_Discord.jpg https://media.discordapp.net/attachments/810490718979489845/812665575116767242/unknown.png https://media.discordapp.net/attachments/810490718979489845/814660396182798357/Screenshot_20210226-094921_Discord.jpg https://media.discordapp.net/attachments/812665665437696020/821039634528206888/unknown-221.png https://media.discordapp.net/attachments/812665665437696020/822043886247084062/EvTv-Z1VgAIHSSb.png https://media.discordapp.net/attachments/812665665437696020/822044049477337119/unknown.png https://media.discordapp.net/attachments/812665665437696020/823019103563284480/c5e56616821bed73.png https://media.discordapp.net/attachments/812665665437696020/823019460373381150/unknown.png https://media.discordapp.net/attachments/812665665437696020/823019752954921011/unknown.png https://media.discordapp.net/attachments/812665665437696020/823020011245142066/unknown-229.png https://media.discordapp.net/attachments/812665665437696020/823020355093528626/Screenshot_20210312-001425_Discord.png https://media.discordapp.net/attachments/812665665437696020/823020499348619314/unknown.png https://media.discordapp.net/attachments/812665665437696020/825588688871620668/unknown.png https://media.discordapp.net/attachments/812665665437696020/825588867612016700/unknown.png https://media.discordapp.net/attachments/812665665437696020/825590522092453928/unknown.png https://media.discordapp.net/attachments/812665665437696020/825753449274408960/image0.png https://media.discordapp.net/attachments/812665665437696020/825753774244757595/1616583229205.png https://media.discordapp.net/attachments/812665665437696020/825754030516076544/20201208_233824.pnghttps://media.discordapp.net/attachments/812665665437696020/825754281558802472/unknown.png https://media.discordapp.net/attachments/812665665437696020/825755286115581992/20200831_183708.png https://media.discordapp.net/attachments/812665665437696020/825755424404799488/EwBRceUVEAIcEJi.png https://media.discordapp.net/attachments/812665665437696020/825756942978121728/unknown.png https://media.discordapp.net/attachments/812665665437696020/828185141141569546/image0.png https://media.discordapp.net/attachments/812665665437696020/828185570807250944/unknown.png https://media.discordapp.net/attachments/812665665437696020/831110620723806228/Screenshot_20210408-092858_Discord.png https://media.discordapp.net/attachments/812665665437696020/831111449433604106/Screenshot_20210201-022054_Discord.png https://media.discordapp.net/attachments/812665665437696020/831111822273675324/15251124154.png https://media.discordapp.net/attachments/812665665437696020/831111572591214632/ersgerg-2.png https://media.discordapp.net/attachments/812665665437696020/835502919277215794/20210413_001801.png https://media.discordapp.net/attachments/812665665437696020/835503322445119518/unknown.png https://media.discordapp.net/attachments/812665665437696020/835503848625012746/Screenshot_20210401-014739_Discord.png https://media.discordapp.net/attachments/812665665437696020/835504471458185236/unknown-2.png https://twitter.com/kimsmokestack/status/1377980907651407875?s=20 https://twitter.com/charon_kn/status/1360901959092301833?s=20 https://media.discordapp.net/attachments/812665665437696020/835504615692566568/unknown.png https://media.discordapp.net/attachments/812665665437696020/835504700610183208/kio_00000.png https://media.discordapp.net/attachments/812665665437696020/835504760022237244/image0.png https://media.discordapp.net/attachments/812665665437696020/835504843631624192/unknown.png https://media.discordapp.net/attachments/812665665437696020/835505091103686726/unknown.png https://media.discordapp.net/attachments/812665665437696020/835505308519628810/image0.png https://media.discordapp.net/attachments/812665665437696020/835505396549943316/Screenshot_2021-04-13-20-05-00.png https://media.discordapp.net/attachments/812665665437696020/835505619942375434/unknown.png https://media.discordapp.net/attachments/812665665437696020/835505744375316480/unknown-101.png https://media.discordapp.net/attachments/812665665437696020/838074041994444860/unknown.png https://media.discordapp.net/attachments/812665665437696020/837593342267097128/Screenshot_20210430-160944_Discord.jpg https://media.discordapp.net/attachments/812665665437696020/837329560189534238/Screenshot_20210429-203019_Discord.jpg https://media.discordapp.net/attachments/812665665437696020/836567359552094208/Screenshot_20210427-203959_Discord.jpg https://media.discordapp.net/attachments/812665665437696020/836199520559824906/unknown.png https://media.discordapp.net/attachments/812665665437696020/836061250110095410/Screenshot_20210426-110847_Discord.jpg https://media.discordapp.net/attachments/812665665437696020/836061250110095410/Screenshot_20210426-110847_Discord.jpg https://media.discordapp.net/attachments/812665665437696020/835506083702374450/IMG_20191228_080021.png https://media.discordapp.net/attachments/812665665437696020/835505981680254986/unknown.png https://cdn.discordapp.com/attachments/810490718979489845/835860497047486485/MBC_ND_.mp4 https://media.discordapp.net/attachments/812665665437696020/838075367368949781/unknown.png https://media.discordapp.net/attachments/812665665437696020/838075508096106496/unknown.png https://media.discordapp.net/attachments/812665665437696020/838076168514175036/unknown.png https://media.discordapp.net/attachments/812665665437696020/838076239247441980/Screenshot_20210422-115621_Discord.png https://media.discordapp.net/attachments/812665665437696020/838076332775964722/unknown.png https://media.discordapp.net/attachments/812665665437696020/838076543732678678/image0.png https://media.discordapp.net/attachments/812665665437696020/838262172530245662/Screenshot_20210429-134639_Discord.png https://media.discordapp.net/attachments/812665665437696020/838262860491915274/unknown.png https://media.discordapp.net/attachments/812665665437696020/838934122474242118/Screenshot_20210503-174458_Discord.png https://media.discordapp.net/attachments/812665665437696020/839141955908272168/unknown.png https://media.discordapp.net/attachments/812665665437696020/839472996749279232/unknown.png https://media.discordapp.net/attachments/812665665437696020/839537843827114027/2-4.png https://media.discordapp.net/attachments/812665665437696020/839627445879701524/unknown-241.png https://media.discordapp.net/attachments/812665665437696020/839896215575199754/Screenshot_20210507-010710_Discord.jpg https://media.discordapp.net/attachments/812665665437696020/840803559050182676/unknown.png https://media.discordapp.net/attachments/812665665437696020/840803806488952882/PicsArt_05-06-01.png https://media.discordapp.net/attachments/812665665437696020/840803835656273950/unknown.png "
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

TOKEN = os.getenv('BOT_TOKEN')
client.run(TOKEN)
