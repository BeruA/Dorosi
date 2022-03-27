import discord
import random
import asyncio
import time

client = discord.Client()

token = 'OTQ0NDg2ODUyNzM0MzYxNjQw.YhCT7Q.RrIKtjhsjyqvjZHHRy2q--nejno'


# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")
    discord.Game("감자요리")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('상태메시지'))
    await bt(['마감', '응가', '숙면', '식사', '물밥', '하는 중 하는 중 하는 중 하는 중', '게임', '화공', '도발', '섹시'])

async def bt(games):
    await client.wait_until_ready()

    while not client.is_closed():
        for g in games:
            await client.change_presence(status=discord.Status.online, activity=discord.Game(g))
            await asyncio.sleep(1)

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('킥좀 '):
        target = message.mentions[0]
        msg = await channel.send(target.mention + " 추방 투표!!!")
        await msg.add_reaction("🦶") #step
        await msg.add_reaction("💢") #stun

    if message.content.startswith('오백배'):
        target = message.mentions[0]
        await channel.send(target.mention)
        await channel.send(target.mention)
        await channel.send(target.mention)
        await channel.send(target.mention)
        await channel.send(target.mention)

    if message.content.startswith('야! 안녕'):
        await channel.send('반가워 시발아!')

    if message.content.startswith('문어'):
        await channel.send('https://media.discordapp.net/attachments/847126893534117890/944739580270223370/unknown_1.mp4')

    if message.content.startswith('야! 명령어'):
        await channel.send('니가 알아서 찾으셈')

    if message.content.startswith('신작'):
        await channel.send('https://youtu.be/dggymuhfbcI')

    if message.content.startswith('수정'):
        msg = await message.channel.send("안녕하세요")
        await asyncio.sleep(3)
        await msg.edit(content="반갑습니다")

    if message.content.startswith('야! 조배호'):
        anser = "강태산이넘!!!!!!!!!!!!! 오허어ㄲㅈ 멀라훕!!!!! 아이탈당이라니 축하해요ㅎㅎㅎㅎ 음~ 법적으로처리해!"
        anserchoice = anser.split(" ")
        ansernumber = random.randint(1, len(anserchoice))
        anserresult = anserchoice[ansernumber - 1]
        await channel.send(anserresult)

    if message.content.startswith('BPM 레드존'):
        await channel.send('** " 165 " **')

    if message.content.startswith('BPM 에반스'):
        await channel.send('** " 180 " **')

    if message.content.startswith('보고!'):
        await channel.send('보고!')

    if message.content.startswith('충성!'):
        await channel.send('충성이 맞나?')

    if message.content.startswith('청성!'):
        await channel.send('청성!')

    if message.content.startswith('오목'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/909772224985169920/61f6a43cf48d37add2a45df32f82f4d845bf7f3bf7b82e7a731acdc628dba4a3.png')
            
    if message.content.startswith('점호 인원보고 총원'):
        await channel.send('쉬어!')

    if message.content.startswith('큰일'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/901454917221355570/ar10232106.png')

    if message.content.startswith('도로시'):
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/948145013206949918/IMG_2337.png')

    if message.content.startswith('ㅆㅃ'):
        await channel.send('ㅅㅂ')

    if message.content.startswith('님들'):
        await channel.send('왜')

    if message.content.startswith('ㅂㅅ'):
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

    if message.content.startswith('노홍철'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/825755424404799488/EwBRceUVEAIcEJi.png')

    if message.content.startswith('나이'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/825756942978121728/unknown.png')

    if message.content.startswith('짱구'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/829346755551297606/1.png')

    if message.content.startswith('브베'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/835502919277215794/20210413_001801.png')

    if message.content.startswith('할까'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/838075427011821639/Screenshot_20210319-122910_Twitter.png')

    if message.content.startswith('대도'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/839141955908272168/unknown.png')

    if message.content.startswith('톰'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/840803835656273950/unknown.png')

    if message.content.startswith('마리오'):
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/842759365969707058/SPOILER_.mp4')

    if message.content.startswith('귀갱'):
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/842369911045095424/2019_12_13_00_06_53_273.mp4')

    if message.content.startswith('빈모드'):
        await channel.send('https://cdn.discordapp.com/attachments/835782065306992651/846669510752337930/4b2e91c5ed64bc9b.mp4')

    if message.content.startswith('돌'):
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/948183674568966204/unknown.png')

    if message.content.startswith('여유만만'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/853565574457589760/unknown-19.png')

    if message.content.startswith('네류'):
        await channel.send('https://images-ext-1.discordapp.net/external/t8Has7FcLiB1B752L_ndepQTLfsQglqd6oMDJhPGt_Q/https/media.discordapp.net/attachments/491939455993774080/829287313833590804/20210407_182721.gif')

    if message.content.startswith('정모'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/856147263003557898/image0.png')

    if message.content.startswith('오모리'):
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/853612755188711445/23ea8f842119299a.mp4')

    if message.content.startswith('약속'):
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/857269797179228180/oyakusoku.mp4')

    if message.content.startswith('밀집'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/859330982695141376/7185ec6cb2a2a4db43e2bfd5439279371e4d18843e33de31c2bb835d852c8b84.png')

    if message.content.startswith('나츠키'):
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/861979377171169300/SPOILER_064c244122f56a8723a270068f0c8875.png')

    if message.content.startswith('모울'):
        await channel.send('https://cdn.discordapp.com/attachments/828954273005568020/860912532801191976/2021-07-04_00-57-31.mp4')

    if message.content.startswith('수학'):
        await channel.send('https://cdn.discordapp.com/attachments/810490718979489845/860914143594807376/2021-07-04_01-01-55.mp4')

    if message.content.startswith('마크'):
        await channel.send('https://twitter.com/ayylmaotv/status/1117457494920527872?s=20')

    if message.content.startswith('선풍기'):
        await channel.send('https://cdn.discordapp.com/attachments/854352795813150740/866932414286528552/VID-20210630-WA0017.mp4')

    if message.content.startswith('히나'):
        await channel.send('https://media.discordapp.net/attachments/810490718979489845/948168546008051762/Screenshot_20201102-222800_YouTube.jpg')

    if message.content.startswith('다천사'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/868202048598986772/108.png')

    if message.content.startswith('운동'):
        await channel.send('https://images-ext-2.discordapp.net/external/z4ZyZRHrnDayVtxd7w5dzWpt3o7MX3LTbmt-UGvDObk/https/media.discordapp.net/attachments/804829274384498761/939227928535924847/the_boys-4-1.gif')

    if message.content.startswith('미나'):
        await channel.send('https://media.discordapp.net/attachments/860770065568890881/948150755544666153/96F2649C-940F-474C-A07F-B68D9FBCEE50.jpg')

    if message.content.startswith('보지'):
        await channel.send('https://media.discordapp.net/attachments/860770065568890881/948150755544666153/96F2649C-940F-474C-A07F-B68D9FBCEE50.jpg')

    if message.content.startswith('잠만'):
        time.sleep(3)
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/910233954823581776/1157A2C9-38D1-4F53-BA03-0601866107E9.jpg')

    if message.content.startswith('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ'):
        await channel.send('https://media.discordapp.net/attachments/803945796151279636/948146187553361950/IMG_2341.png')

    if message.content.startswith('어쩔티비'):
        await channel.send('저쩔티비')

    if message.content.startswith('치킨'):
        await channel.send('https://media.discordapp.net/attachments/847126944360431646/932275088819118110/dcbest-20220116-230811-001.jpg')

    if message.content.startswith('...'):
        await channel.send('https://media.discordapp.net/attachments/860770065568890881/948146865369669682/2.png')

    if message.content.startswith('에어컨'):
        await channel.send('https://media.discordapp.net/attachments/812665665437696020/910366135571083345/received_343331183966812.jpeg')

    if message.content.startswith("**조배호**"):
        await channel.send('https://cdn.discordapp.com/attachments/561510770723127309/867291290106331136/video0.mp4https://cdn.discordapp.com/attachments/561510770723127309/867291290466779176/video1.mp4https://cdn.discordapp.com/attachments/561510770723127309/867291290797735956/video2.mp4')

@client.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "🦶":
        await reaction.message.channel.send(user.name + " : 킥 ㄱ")
    if str(reaction.emoji) == "💢":
        await reaction.message.channel.send(user.name + " : 밴 ㄱ")
    if str(reaction.emoji) == "👍":
        await reaction.message.channel.send("굳이요")
    if str(reaction.emoji) == "💣":
        await reaction.message.channel.send("https://youtu.be/hlR45geEIpY")
    if str(reaction.emoji) == "🇨🇳":
        await reaction.message.channel.send("https://cdn.discordapp.com/attachments/884787722819092521/908537510974615572/SPOILER_super_idol_.mp4")





client.run('OTQ0NDg2ODUyNzM0MzYxNjQw.YhCT7Q.RrIKtjhsjyqvjZHHRy2q--nejno')
