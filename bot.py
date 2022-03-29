import discord
import random
import asyncio
import time
import os
import io
import shutil
import schedule
import time
import datetime
import itertools
from discord.ext import tasks

from google_images_download import google_images_download
from PIL import Image, ImageDraw, ImageFont, ImageOps

client = discord.Client(
    intents=discord.Intents.all()
)

    
# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")
    
    ids = [
        810490718979489845,
        772475285320237069,
        853846368870596688,
        ]
    channels = [client.get_channel(id) for id in ids]
    
    for ch in channels:
        await ch.send("크로니콥터가 착륙했어!")
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
        847126893534117890,
    ]
    channels = [client.get_channel(id) for id in ids]  
    now = datetime.datetime.now()

    if now.hour == 18 and now.minute == 0 and now.second == 0:
        for ch in channels:
            await ch.send("https://youtu.be/H04dl1te52Q")

    if now.hour == 8 and now.minute == 30 and now.second == 0:
        for ch in channels:
            await ch.send("구닌들 폰 받는시간!!")
    
    if now.hour == 12 and now.minute == 0 and now.second == 0:
        for ch in channels:
            await ch.send("구닌들 폰 내는시간ㅠㅠ")

    if now.hour == 13 and now.minute == 13 and now.second == 0:
        for ch in channels:
            await ch.send("https://media.discordapp.net/attachments/803945796151279636/958309861903458324/IMG_2999.png")

    if now.hour == 22 and now.minute == 0 and now.second == 0:
        for ch in channels:
            await ch.send("https://media.discordapp.net/attachments/803945796151279636/958309862691975198/IMG_2996.png")
            

channels_500x_enabled = []

@client.event
async def on_message(message):
    global is_500x_enabled
    channel = message.channel

    if message.author.bot:
        return None
        
    if message.content == ('에고'):
        await message.delete()
        await channel.send('https://media.discordapp.net/attachments/956643812883697704/958361371416879214/IMG_3016.png')
        await channel.send('아첨해대는그모습구역질이날것같아시니컬한시선의비오늘도두눈을닫는척')

    if message.content == (' '):
        p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'm', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        if random.choice(p) == ('a'):
            await message.delete()
            await channel.send('축하합니다! 당신은 5% 확률에 걸렸습니다! 다음엔 조용히 얘기해주세요!!!!!')
        else:
            return

    if '킥' in message.content:                
        if not message.mentions:
            return
        target = message.mentions[0]
        msg = channel.send(target.mention + " 추방 투표!!!")
        await msg.add_reaction("🦶") #step
        await msg.add_reaction("💢") #stun

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

    if message.content.startswith('눈나'):
        await channel.send('https://images-ext-1.discordapp.net/external/sWESaX7qOJS0n8xmLrCH1cxhzBfO1ojC4KHHEbf6P-E/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/Fh58fxSBt08AAAPo/ouro-kronii-wink.mp4')

    if 'ㅇㅎ' in message.content:
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/957662414378270761/unknown-23.png')

    if message.content == ('다'):
        await channel.send('다섯살짜리리리리~리리리짜리짜리어린애로있는구나나나나나나나나네이름은짱구신짱구짱구짱구짱구다섯살짜리리리리~리리리짜리짜리어린애로근데당신기타사무라이면서못된괴물이로구나~!신짱구받아라라라라라라라라라라라라라라라라라라라라라라라라음~해보셔도동가동동동모든버튜버중가장귀여운건누구냐?페코짱~도동가동동동동동동모든버튜버중청초한건누구냐?AhoyAhoyHowareyou아임허니아아아아아여러분!오늘새친구가왔어요알피..?ㅈ까!(도망감)대단하구나!(디스)알피는방에서놀고싶어요띠용띠용분명히...레이니일꺼야야!레이니!널사랑해...!있잖아..오빤...정말좋은오빠야!들어와엄마!너답게행동하면돼(ㅅㅂ)삼각산정기받은서울중앙에~김상덕호우후론트라라후론트라라후론트라라라라라라라라거40년을넘게바퀼라에몸담아왔으니모두넘겨!뇨뇨뇨내욕망의검은손으로널먹어주겠어..흐와아아(미친음조절)하?오르카를어떻게생각하고있는거야?멍청이!도둑놈!기생오라비!슷키리시타아마사다코코아와반호텐노모노오시요시타카나?데타!소레와소레와파파파파파팡스테키나키다이다네키다이다네에에에어서오세요~나는매운거진짜못먹는다특산품도잔뜩들어있는걸?특산품?으아아아!이번엔딸국질이야?헉?헉?어뜩하노준비됐지?어때멈췄어..?끅나라야네나라야~네!나라야!!!부산언니!나라야!!!!!!!!!갑니다아아아가짜?내가가짜?도시락을보여다오!!!!!!!!!!!마고마해라~보영아이번에이사하면서짐정리하는거많이힘들었을텐데내가좀부족하지만많이도와줄게오지마!마마마마사랑아보영해사람아보행해할아버지응애산와머니중국정부에게중국말로한마디하세요ㅈ같다ㅗ렛츠,고도리!나야말로진짜영웅왕중의왕너처럼가짜영웅이아니라고!4번째는너랑께?빵상?뿌뿌뿡!뚝배기!야아아아아아!감성보다이성이날앞선OHNO!눈뒤집어까가지고55도발왜?왜!안죄송해!뭉탱이로있다가유링게슝?아이고난!여러분이거다거짓말인거아시죠!이집짬뽕잘한다어디서시켰어?받아롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸졌다~!')

    if message.content == ('엄'):
        await channel.send('https://media.discordapp.net/attachments/847126893534117890/957883016984809532/hqdefault.png')

    if message.content.startswith('명령어'):
        await channel.send('니가 알아서 찾으셈')

    if message.content.startswith('신작'):
        await channel.send('https://youtu.be/dggymuhfbcI')

    if '사랑해' in message.content:
        if not message.mentions:
            return

        target = message.mentions[0]
        msg = await message.channel.send(target.mention + " 사랑해💕💕")
        await asyncio.sleep(5)
        await msg.edit(content=target.mention + " 사망해💀💀")

    if '신보물섬' in message.content:
        anser = "https://media.discordapp.net/attachments/812665665437696020/898653973278519296/Screenshot_20210601-010856_Discord-Beta.jpg https://media.discordapp.net/attachments/812665665437696020/898653973018464286/Screenshot_20210601-010649_Discord-Beta.jpg https://media.discordapp.net/attachments/812665665437696020/898653972775182336/Screenshot_20210601-010451_Discord-Beta.jpg https://media.discordapp.net/attachments/812665665437696020/848574318635646976/image0.png https://twitter.com/kimsmokestack/status/1377980907651407875?s=20 https://media.discordapp.net/attachments/812665665437696020/828185570807250944/unknown.png https://media.discordapp.net/attachments/812665665437696020/825590522092453928/unknown.png"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

    if '보지' in message.content:
        anser = "https://media.discordapp.net/attachments/812665665437696020/875257614034935858/image0.png https://media.discordapp.net/attachments/812665665437696020/875257572763004968/image0.png https://media.discordapp.net/attachments/812665665437696020/874583000237621318/image0.png https://media.discordapp.net/attachments/812665665437696020/874582923980972071/image0.png https://media.discordapp.net/attachments/812665665437696020/874582720469168168/image0.png https://media.discordapp.net/attachments/812665665437696020/874582678794559528/image0.png"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

    if '배호' in message.content:
        anser = "멀라훕! https://media.discordapp.net/attachments/797862892291751978/798195017416048651/ErctcYFVgAA_BsH.png https://media.discordapp.net/attachments/889488917278113792/889941784078204938/unknown-462.png https://media.discordapp.net/attachments/812665665437696020/909799908138156062/Screenshot_20211115-022709_YouTube.png https://media.discordapp.net/attachments/812665665437696020/856145724789358592/unknown.png https://media.discordapp.net/attachments/812665665437696020/846007050873602058/unknown.png"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

    if '유재석' in message.content:
        anser = "https://media.discordapp.net/attachments/812665665437696020/898533166854316053/unknown.png https://media.discordapp.net/attachments/812665665437696020/890923027200626768/9241913.png https://media.discordapp.net/attachments/812665665437696020/882953006138683392/image0-22.png https://images-ext-2.discordapp.net/external/ouappJrhNvu16WMAh_EphQitPgXDvevv9RvDtoa5x18/https/media.discordapp.net/attachments/810490718979489845/868899031160590378/unknown.png https://media.discordapp.net/attachments/812665665437696020/846007156904951808/unknown.png https://media.discordapp.net/attachments/812665665437696020/838076543732678678/image0.png"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

    if '먹지' in message.content:
        anser = "굶어 먹지마 죽어 치킨 피자 떡볶이"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

    if '만기' in message.content:
        anser = "꿀벌 https://media.discordapp.net/attachments/847126893534117890/958242108651765770/unknown-2-removebg-preview.png https://images-ext-1.discordapp.net/external/VFj_87_XFzhA4udB35lrkMoo03VcfUO3RI-FjBsmafA/https/media.discordapp.net/attachments/847126893534117890/958240426320609320/projectmx-20220328-172436-000.jpg.jpg"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

    if '어쩔티비' in message.content:
        await channel.send('저쩔티비')

    if '어떨까요' in message.content:
        await message.delete()
        await channel.send('https://media.discordapp.net/attachments/847126893534117890/958242582922690561/IMG_2992.png')

    if '폐업' in message.content:
        await channel.send('https://media.discordapp.net/attachments/840125539700178954/957666023627182140/20220322_171605.jpg')

    if '아이고' in message.content:
        await channel.send('https://media.discordapp.net/attachments/792743630140866572/792759057060200488/32709ee9-0d73-4ac4-82ce-9266e6ff7700216w640.png')

    if '솔로이스트' in message.content:
        await channel.send('https://media.discordapp.net/attachments/783003781935792139/787583175312146432/99A2CA455B85FBB208.png')

    if '자취' in message.content:
        await channel.send('https://media.discordapp.net/attachments/746389180720087051/782663158799007754/image0.png')

    if '이현호' in message.content:
        await channel.send('https://media.discordapp.net/attachments/746389180720087051/775341921324761088/unknown_copy.png')

    if '극장판' in message.content:
        await channel.send('1기 액션가면VS그레그레마왕\n2기 부리부리왕국의 보물\n3기 흑부리 마왕의 야망\n4기 핸더랜드의 대모험\n5기 암흑마왕 대추적\n6기 돼지발굽 대작전\n7기 폭발 온천 부글부글 대작전\n8기 폭풍을 부르는 정글\n9기 어른제국의 역습\n10기 태풍을 부르는 장엄한 전설의 결투\n11기 태풍을 부르는 영광의 불고기로드\n12기 폭풍을 부르는 석양의 떡잎마을방범대\n13기 전설을 부르는 부리나케 딱 3분 대진격\n14기 전설을 부르는 전설의 춤을춰라 아미고\n15기 전설을 부르는 노래하는 엉덩이 폭탄\n16기 엄청난 태풍을 부르는 금창의 용사\n17기 떡잎마을 야생왕국\n18기 초시공 전설을 부르는 아우라의 신부\n19기 황금스파이 대작전\n20기 폭풍을 부르는 나와 우주의 프린세스\n21기:크레용신짱! 바카우마츠! B급 음식 서바이벌!\n﻿22기:검은태풍을 부르는 엄청난양의 보물!!\n23기:태풍을 부르는 엄청난 양의 보물\n24기:전설을 부르는 파이어의 비밀\n25기:멸망의카운트다운! 파괴의 기계대전!!\n26기:태풍을부르는 검은 암살자의 대소동\n27기: 영광의 액션가면 vs 구리구리몬\n28기:죽음을 부르는 검은 무사기사단\n29기:검은태풍을 부르는 떡잎마을 파괴사건\n30기:태풍을 부르는 알수없는 그림자\n31기:전설을 부르는 1개의 빛의 열쇠\n32기:엄청난 태풍을 부르는 빛의 거울의 진실\n33기:엄청난 파괴를 알리는 3개의 원자폭탄\n34기:엄청난 위험을 부르는 괴물 대소동\n35기:얼수없는 1명의 칼을든 사나이\n36기:엄청난 태풍을 부르는 액션가면 조종사건\n37기:위험을 알리는 3명의무사단\n38기:엄청난 태풍을 부르는 1명의 연금술사\n39기:알수없는 인간실종사건의 진실\n40기:위험을 알리는 짱구가족 죽음의 진실\n41기:엄청난 태풍을 부르는 짱구와 휜둥이의 짱아 구출 대사건\n42기:태풍을 부르는 짱구의 비밀기지\n43기:알수없는 총을든 3명의 특공대\n44기:짱구가족 사람 살인사건﻿\n45기:알수없는 인간 조종사의 진실\n46기:피할수 없는 지구 멸망사건\n47기:엄청난 태풍을 부르는 쥬라기 시대 대소동\n48기:검은태풍을 부르는 멸망의 원석\n49기:떡잎방위대의 1개의 트라포이스\n50기:태풍을 부르는 지구 인간 실종사건\n51기:태풍을 부르는 짱구 영화속의 사람 출동\n52기: 엄청난 영광의 흰둥이 괴물사건')

    if '비주얼' in message.content:
        await channel.send('https://media.discordapp.net/attachments/847126893534117890/957888482389418014/f237ac463a108bddef9ea15b08f63d1f.PNG')

    if '곰' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/816677434866270258/Screenshot_20210303-232421_Discord.jpg')

    if '엄마' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/821039634528206888/unknown-221.png')

    if '북두' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/825588688871620668/unknown.png')

    if '마약' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/825588867612016700/unknown.png')

    if '달팽이' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/831110620723806228/Screenshot_20210408-092858_Discord.png')

    if '말종' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/831111572591214632/ersgerg-2.png')

    if '면접' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/831111822273675324/15251124154.png')

    if '운지' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/846007444416364554/-Xz6gjxfSwWEPbJGvTom6JJKeWdkXOl3QT2sWYPvGMUJnH2k0iMq501t4dzVsosJPqmGQ8S3R6-4LaRZv9EqF9nEQhdpoy4L_nn-.png')

    if '혼자' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/848574228830617610/image0.png')
    
    if '내신' in message.content:
        await channel.send('https://media.discordapp.net/attachments/847126893534117890/901130523118829598/ar0030.png')

    if '종이' in message.content:
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/889474470568427560/20201202_134238.jpg')

    if '슈' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/859329369359908884/Screenshot_20210627-071738_Discord-Beta.png')

    if '강태산' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/859331627263328256/unknown.png')

    if '샤를' in message.content:
        await channel.send('https://youtu.be/szWb4X3JhQs')

    if '베리나' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/868908849174806588/Screenshot_20210624-114233_Parallel_Space_64Bit_Support.jpg')

    if '가!!' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/868908611856900176/Screenshot_20210625-163419_Discord-Beta.jpg')

    if '동땡' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/868908369954635806/Screenshot_20200826-201901_Chrome.jpg')

    if '강현' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/868908370197872640/Screenshot_20200826-201955_Chrome.jpg')

    if '소방' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/868911950287994910/Screenshot_20210701-021422_Discord-Beta.jpg')

    if '타자' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/699297048620433408/865598554583072838/bandicam_2021-07-16_23-18-34-873.mp4')

    if '탄수' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/871781895522893844/unknown.png')

    if '좆기' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/880134617108213851/Capture_2019-06-14-07-19-01-2.png')

    if '버튜버' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/881176304672702504/anigif1.gif')

    if '해부' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/879628600515641415/Screenshot_20210824-112925.jpg')

    if '배드애플' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/878669540127571978/unnamed-15.jpg')

    if '보성' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/877055015582318622/SmartSelect_20210810-181658_YouTube.png')

    if '문재인' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/855418856796192810/881577768599552070/video0.mp4')

    if '논논' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/884410105062387723/unknown.png')

    if '원본' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/885162564739268638/Screenshot_20210908-224437_YouTube.jpg')

    if '도날드' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/886257277970042940/20210911_232146.jpg')

    if '란란루' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/886257277970042940/20210911_232146.jpg')

    if '자위' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/886272376290041906/unknown-190.png')

    if '터짐' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/888660612685643776/Screenshot_20210918-143146_Discord-Beta.jpg')

    if '짚' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/888801542499602472/unknown.png')

    if '렘' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/890774542207832124/Screenshots_2021-08-02-23-25-06.png')

    if '리퍼' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/891504355612721192/unknown.png')

    if '포켓몬' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/894395903811649546/Untitled-1.png')

    if '레드존' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/856781757546102795/896473145890979860/ertert-1.mp4')

    if '지메' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/220651459237249024/899300601341571102/geometry_dash.mp4')

    if '오기' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/900402987002896394/unknown.png')

    if '댄로댄' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/900443260550524938/07-23_SD_360p_MEDIUM_FR30.mp4')

    if '배신' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/901112663025790996/unknown.png')

    if '백신' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/901125247032492042/ar10222335.png')

    if '진배' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/901125245623238737/ar110222345.png')

    if '류담' in message.content:
        await channel.send('둥탁뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅자여러분안녕하십니까달인을만나다의류담입니다오늘이시간에는십육년동안악기를연구해오신해오신악기의달인뮤뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅뱅모든생활용품들을다연주가가능하신거죠?아알겠습니다그러면자여기숟가락이것도가능하세요?무엇이무엇이무엇이똑같을까자여기서배에힘을주고아아아아아아아아아아아아아둥둥둥탕탕탕탕뽀오얀담배연기화려한차림속에호올로비쳐진내애에히릿초라하아안수평안에세월속')

    if '고추' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/914206441655640094/unknown.png')

    if '지니어스' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/910955822245380136/Screenshot_20210823-211619_Discord-Beta.jpg')

    if '토론' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/910728523830943796/Screenshot_20211118-115759_Drive.png')

    if '땜빵' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/909764676492099644/unknown.png')

    if '작업' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/908722808996122694/unknown.png')

    if '보추' in message.content:
        await channel.send('https://media.discordapp.net/attachments/847126944360431646/906985872904290304/unknown.png')

    if message.content.startswith('보고!'):
        await channel.send('보고!')

    if message.content.startswith('충성!'):
        await channel.send('충성이 맞나?')

    if message.content.startswith('청성!'):
        await channel.send('청성!')

    if '오목' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/909772224985169920/61f6a43cf48d37add2a45df32f82f4d845bf7f3bf7b82e7a731acdc628dba4a3.png')
            
    if message.content.startswith('점호 인원보고 총원'):
        await channel.send('쉬어!')

    if '일남' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/901454917221355570/ar10232106.png')

    if 'ㄲㅂ' in message.content:
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/957690701473271808/IMG_2883.jpg')

    if message.content.startswith('ㅆㅃ'):
        await channel.send('ㅅㅂ')

    if '님들' in message.content:
        await channel.send('왜')

    if message.content == ('ㅂㅅ'):
        await channel.send('어휴ㅉㅉㅉㅉ')

    if message.content.startswith('허벌'):
        await channel.send('합성계 최고 허벌후장대회가 열렸다. 예선 경기 끝에 남은 것은 김굴뚝, 큐브1171, 류한수 세 명이었다.')
        time.sleep(2)
        await channel.send('결승전 경기는 자유종목이었고, 각자 후장 안에 가장 커다란 걸 집어넣어 온 선수가 승리하는 것으로 결정됐다.')
        time.sleep(2)
        await channel.send('첫 선수인 김굴뚝이 가랑이를 벌리자 안에서 한조각이 기어나왔다 그러고선 관객과 심사위원들로부터 우레와 같은 박수갈채가 쏟아져 나왔다.')
        time.sleep(2)
        await channel.send('그 후, 큐브1171이 가랑이를 벌렸다. 아무런 것도 나오지 않자 관객들이 의아해 하자, 멀라훕거리는 소리가 들리기 시작했다. 그러자 조배호가 큐브1171의 후장에서 민우당 중진들과 함께 튀어나와 대회장 밖으로 사라졌다. 관객들은 대단하다는 반응과 더럽다는 반응이 섞인 모습이었다.')
        time.sleep(4)
        await channel.send('마지막은 류한수의 차례였다. 하지만 류한수 가랑이 사이에서 나온건 조그만 김된장 하나뿐이지 않은가? 다른 참가자들은 류한수를 비웃으며 손가락질 했다.')
        time.sleep(2)
        await channel.send('그러자 김된장은 유쾌하게 자기가 나온 구멍을 가리키며 외쳤다.')
        time.sleep(5)
        await channel.send('**“월곶탐험에 오신 걸 환영합니다!!”**')

    if '노홍철' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/825755424404799488/EwBRceUVEAIcEJi.png')

    if '나이' in message.content:
        if '나이스' in message.content:
            return
        else:
            await channel.send('https://media.discordapp.net/attachments/812665665437696020/825756942978121728/unknown.png')

    if '짱구' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/829346755551297606/1.png')

    if '브베' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/835502919277215794/20210413_001801.png')

    if '할까' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/838075427011821639/Screenshot_20210319-122910_Twitter.png')

    if '대도' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/839141955908272168/unknown.png')

    if '톰' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/840803835656273950/unknown.png')

    if '마리오' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/842759365969707058/SPOILER_.mp4')

    if '귀갱' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/842369911045095424/2019_12_13_00_06_53_273.mp4')

    if '빈1모드' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/835782065306992651/846669510752337930/4b2e91c5ed64bc9b.mp4')

    if message.content == '돌':
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/948183674568966204/unknown.png')

    if message.content == '여유만만':
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/853565574457589760/unknown-19.png')

    if '네류' in message.content:
        await channel.send('https://images-ext-1.discordapp.net/external/t8Has7FcLiB1B752L_ndepQTLfsQglqd6oMDJhPGt_Q/https/media.discordapp.net/attachments/491939455993774080/829287313833590804/20210407_182721.gif')

    if '정모' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/856147263003557898/image0.png')

    if '오모리' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/853612755188711445/23ea8f842119299a.mp4')

    if '약속' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/857269797179228180/oyakusoku.mp4')

    if '밀집' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/859330982695141376/7185ec6cb2a2a4db43e2bfd5439279371e4d18843e33de31c2bb835d852c8b84.png')

    if '나츠키' in message.content:
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/861979377171169300/SPOILER_064c244122f56a8723a270068f0c8875.png')

    if '모울' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/828954273005568020/860912532801191976/2021-07-04_00-57-31.mp4')

    if '수학' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/860914143594807376/2021-07-04_01-01-55.mp4')

    if '마크' in message.content:
        await channel.send('https://twitter.com/ayylmaotv/status/1117457494920527872?s=20')

    if '선풍기' in message.content:
        await channel.send('https://cdn.discordapp.com/attachments/854352795813150740/866932414286528552/VID-20210630-WA0017.mp4')

    if '히나' in message.content:
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/948168546008051762/Screenshot_20201102-222800_YouTube.jpg')

    if '다천사' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/868202048598986772/108.png')

    if '운동' in message.content:
        await channel.send('https://images-ext-2.discordapp.net/external/z4ZyZRHrnDayVtxd7w5dzWpt3o7MX3LTbmt-UGvDObk/https/media.discordapp.net/attachments/804829274384498761/939227928535924847/the_boys-4-1.gif')

    if '미나' in message.content:
        await channel.send('https://media.discordapp.net/attachments/860770065568890881/948150755544666153/96F2649C-940F-474C-A07F-B68D9FBCEE50.jpg')

    if message.content.startswith('잠만'):
        time.sleep(3)
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/910233954823581776/1157A2C9-38D1-4F53-BA03-0601866107E9.jpg')

    if message.content.startswith('ㄱㅋㄲ'):
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/948146187553361950/IMG_2341.png')

    if '까비' in message.content:
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/957690701473271808/IMG_2883.jpg')

    if '치킨' in message.content:
        await channel.send('https://media.discordapp.net/attachments/847126944360431646/932275088819118110/dcbest-20220116-230811-001.jpg')

    if message.content.startswith('...'):
        await channel.send('https://media.discordapp.net/attachments/860770065568890881/948146865369669682/2.png')

    if '에어컨' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/910366135571083345/received_343331183966812.jpeg')

    if message.content.startswith("**조배호**"):
        await channel.send('https://cdn.discordapp.com/attachments/561510770723127309/867291290106331136/video0.mp4 https://cdn.discordapp.com/attachments/561510770723127309/867291290466779176/video1.mp4 https://cdn.discordapp.com/attachments/561510770723127309/867291290797735956/video2.mp4')

@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "👍":
        await reaction.message.channel.send("굳이요")
    if not reaction.message.author.bot or user.bot:
        return
    if str(reaction.emoji) == "🦶":
        await reaction.message.channel.send(user.name + " : 킥 ㄱ")
    if str(reaction.emoji) == "💢":
        await reaction.message.channel.send(user.name + " : 밴 ㄱ")
    if str(reaction.emoji) == "💣":
        await reaction.message.channel.send("https://youtu.be/hlR45geEIpY")
    if str(reaction.emoji) == "🇨🇳":
        await reaction.message.channel.send("https://cdn.discordapp.com/attachments/884787722819092521/908537510974615572/SPOILER_super_idol_.mp4")

TOKEN = os.getenv('BOT_TOKEN')
client.run(TOKEN)
