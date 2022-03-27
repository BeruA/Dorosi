import discord
import random
import asyncio
import time
import os

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

    await client.change_presence(status=discord.Status.idle, activity=discord.Game('상태메시지'))
    await bt(['마감', '숙면', '식사', '하는 중 하는 중 하는 중 하는 중', '게임', '화공', '도발', '섹스'])

async def bt(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status=discord.Status.online, activity=discord.Game(g))
            await asyncio.sleep(10)

@client.event
async def on_message(message):
    channel = message.channel
    global is_500x_enabled

    if message.author.bot:
        return None

    if '킥' in message.content:
        if not message.mentions:
            return

        target = message.mentions[0]
        msg = await channel.send(target.mention + " 추방 투표!!!")
        await msg.add_reaction("🦶") #step
        await msg.add_reaction("💢") #stun

    if '오백배' in message.content:
        if not message.mentions:
            return

        target = message.mentions[0]
        is_500x_enabled = True
        for i in range(500):
            if not is_500x_enabled:
                return
            await channel.send(target.mention)
            await asyncio.sleep(3)

    if 'ㅅㅂ' in message.content and is_500x_enabled:
        await channel.send('ㅈㅅ')
        is_500x_enabled = False
        return

    if '조배호' in message.content:
        await channel.send('https://media.discordapp.net/attachments/889488917278113792/889941784078204938/unknown-462.png')

    if message.content.startswith('눈나'):
        await channel.send('https://images-ext-1.discordapp.net/external/sWESaX7qOJS0n8xmLrCH1cxhzBfO1ojC4KHHEbf6P-E/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/Fh58fxSBt08AAAPo/ouro-kronii-wink.mp4')

    if 'ㅇㅎ' in message.content:
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/957662414378270761/unknown-23.png')

    if message.content.startswith('다'):
        await channel.send('다섯살짜리리리리~리리리짜리짜리어린애로있는구나나나나나나나나네이름은짱구신짱구짱구짱구짱구다섯살짜리리리리~리리리짜리짜리어린애로근데당신기타사무라이면서못된괴물이로구나~!신짱구받아라라라라라라라라라라라라라라라라라라라라라라라라음~해보셔도동가동동동모든버튜버중가장귀여운건누구냐?페코짱~도동가동동동동동동모든버튜버중청초한건누구냐?AhoyAhoyHowareyou아임허니아아아아아여러분!오늘새친구가왔어요알피..?ㅈ까!(도망감)대단하구나!(디스)알피는방에서놀고싶어요띠용띠용분명히...레이니일꺼야야!레이니!널사랑해...!있잖아..오빤...정말좋은오빠야!들어와엄마!너답게행동하면돼(ㅅㅂ)삼각산정기받은서울중앙에~김상덕호우후론트라라후론트라라후론트라라라라라라라라거40년을넘게바퀼라에몸담아왔으니모두넘겨!뇨뇨뇨내욕망의검은손으로널먹어주겠어..흐와아아(미친음조절)하?오르카를어떻게생각하고있는거야?멍청이!도둑놈!기생오라비!슷키리시타아마사다코코아와반호텐노모노오시요시타카나?데타!소레와소레와파파파파파팡스테키나키다이다네키다이다네에에에어서오세요~나는매운거진짜못먹는다특산품도잔뜩들어있는걸?특산품?으아아아!이번엔딸국질이야?헉?헉?어뜩하노준비됐지?어때멈췄어..?끅나라야네나라야~네!나라야!!!부산언니!나라야!!!!!!!!!갑니다아아아가짜?내가가짜?도시락을보여다오!!!!!!!!!!!마고마해라~보영아이번에이사하면서짐정리하는거많이힘들었을텐데내가좀부족하지만많이도와줄게오지마!마마마마사랑아보영해사람아보행해할아버지응애산와머니중국정부에게중국말로한마디하세요ㅈ같다ㅗ렛츠,고도리!나야말로진짜영웅왕중의왕너처럼가짜영웅이아니라고!4번째는너랑께?빵상?뿌뿌뿡!뚝배기!야아아아아아!감성보다이성이날앞선OHNO!눈뒤집어까가지고55도발왜?왜!안죄송해!뭉탱이로있다가유링게슝?아이고난!여러분이거다거짓말인거아시죠!이집짬뽕잘한다어디서시켰어?받아롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸롸졌다~!')

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

    if '먹지' in message.content:
        anser = "굶어 먹지마 죽어 치킨 피자 떡볶이"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

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

    if message.content.startswith('도로시'):
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/948145013206949918/IMG_2337.png')

    if message.content.startswith('ㅆㅃ'):
        await channel.send('ㅅㅂ')

    if '님들' in message.content:
        await channel.send('왜')

    if 'ㅂㅅ' in message.content:
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

    if '여유만만' inmessage.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/853565574457589760/unknown-19.png')

    if '네류' in message.content:
        await channel.send('https://images-ext-1.discordapp.net/external/t8Has7FcLiB1B752L_ndepQTLfsQglqd6oMDJhPGt_Q/https/media.discordapp.net/attachments/491939455993774080/829287313833590804/20210407_182721.gif')

    if '정모' on message.content:
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

    if '미니' in message.content:
        await channel.send('https://media.discordapp.net/attachments/860770065568890881/948150755544666153/96F2649C-940F-474C-A07F-B68D9FBCEE50.jpg')

    if '보지' in message.content:
        await channel.send('https://media.discordapp.net/attachments/860770065568890881/948150755544666153/96F2649C-940F-474C-A07F-B68D9FBCEE50.jpg')

    if message.content.startswith('잠만'):
        time.sleep(3)
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/910233954823581776/1157A2C9-38D1-4F53-BA03-0601866107E9.jpg')

    if message.content.startswith('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ'):
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/948146187553361950/IMG_2341.png')

    if '어쩔티비' in message.content:
        await channel.send('저쩔티비')

    if '치킨' in message.content:
        await channel.send('https://media.discordapp.net/attachments/847126944360431646/932275088819118110/dcbest-20220116-230811-001.jpg')

    if message.content.startswith('...'):
        await channel.send('https://media.discordapp.net/attachments/860770065568890881/948146865369669682/2.png')

    if '에어컨' in message.content:
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/910366135571083345/received_343331183966812.jpeg')

    if message.content.startswith("**조배호**"):
        await channel.send('https://cdn.discordapp.com/attachments/561510770723127309/867291290106331136/video0.mp4https://cdn.discordapp.com/attachments/561510770723127309/867291290466779176/video1.mp4https://cdn.discordapp.com/attachments/561510770723127309/867291290797735956/video2.mp4')

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
