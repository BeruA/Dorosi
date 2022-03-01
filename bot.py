import discord
import random
import asyncio
import time

client = discord.Client()

token = 'OTQ0NDg2ODUyNzM0MzYxNjQw.YhCT7Q.vYSMAmFvcrGNynK9oMb4yK014XE'


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

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    channel = message.channel
    message.content

    if message.author.bot:
        return None

    if message.content.startswith('!킥'):
        target = message.mentions[0]
        msg = await message.channel.send(target.mention + " 추방 투표!!!")
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

    if message.content == "수정":
        msg = await message.channel.send("안녕하세요")
        await asyncio.sleep(3)
        await msg.edit(content="반갑습니다")

    if message.content.startswith('야! 주사위'):
        await channel.send('데구르르르르르르르')
        time.sleep(2)
        dice = 0
        dice = dice + random.randint(1, 6)
        dice = str(dice)
        await channel.send("" + dice + "!!!!!")

    if message.content.startswith('야! 사다리타기'):
        await channel.send('따라다라 딴! 딴!')
        time.sleep(0.5)
        await channel.send('따라다라 딴! 딴!')
        time.sleep(0.5)
        await channel.send('따라다라 따라라라...')
        time.sleep(2)
        team = message.content[9:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await channel.send("`" + person[i] + "` 넌 `" + teamname[i] + "` 일로가")

    if message.content.startswith('야! 골라'):
        choice = message.content.split(" ")
        choicenumber = random.randint(2, len(choice) - 1)
        choiceresult = choice[choicenumber]
        await channel.send('코카콜라 맛있다')
        time.sleep(0.5)
        await channel.send('맛있으면 또 먹어')
        time.sleep(0.5)
        await channel.send('또 먹으면 배탈나')
        time.sleep(0.5)
        await channel.send('척척박사님 알아맞춰보세요')
        time.sleep(0.5)
        await channel.send('딩동댕동')
        await channel.send("`" + choiceresult + "`코코스키")

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

    if message.content.startswith('야! ㅅㅂㅁㅌ'):
        embed = discord.Embed(title="다으 다으다으다으 다으다으 짠 짠짠 짠짠짠 짠짠짠 서~해~물~과", description="날씨 맑은 완행선 왕복열차에",
                              color=0xFC67E0)
        embed.set_footer(text="마음약해서 잡지못했네")
        embed.set_image(url="https://i.imgur.com/kQlO1d4.png")
        await channel.send(embed=embed)

    elif message.content.startswith('야! 즘킂'):
        await channel.send('왜')

        def pred(m):
            return m.author == message.author and m.channel == message.channel

        try:

            msg = await client.wait_for('message', check=pred, timeout=2.0)
        except asyncio.TimeoutError:
            await channel.send('불러놓고 말을 안해;;')
        else:
            await channel.send('{0.content}'.format(msg))

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
        await channel.send('https://cdn.discordapp.com/attachments/383295111951548437/867050775426105384/trev.mp4 https://cdn.discordapp.com/attachments/383295111951548437/867050780539355196/trev_.mp4 https://cdn.discordapp.com/attachments/383295111951548437/867050789067292682/trev.mp4')


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





client.run('OTQ0NDg2ODUyNzM0MzYxNjQw.YhCT7Q.vYSMAmFvcrGNynK9oMb4yK014XE')
