import discord
import random
import asyncio
import time

client = discord.Client()

# 생성된 토큰을 입력해준다.



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


# 메시지에 반응 달면 체팅해줌
@client.event
async def on_reaction_add(reaction):
    if str(reaction.emoji) == "👍":
        await reaction.message.channel.send("굳이요")

    if str(reaction.emoji) == "👏":
        await reaction.message.channel.send("8888888888888888888888")

    if str(reaction.emoji) == "😭":
        await reaction.message.channel.send("ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ")

    if str(reaction.emoji) == "🖕":
        await reaction.message.channel.send("ㅗ")

    if str(reaction.emoji) == "👀":
        await reaction.message.channel.send("띠용?")

    if str(reaction.emoji) == "🤔":
        await reaction.message.channel.send("흠......")


# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    channel = message.channel
    message.content

    if message.author.bot:
        return None

    if message.content.startswith('야! 안녕'):
        await channel.send('반가워 시발아!')

    if message.content.startswith('야! 명령어'):
        await channel.send('니가 알아서 찾으셈')

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

    if message.content.startswith("야! 사다리타기"):
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



client.run("ODkzMTcwMTQyODI4MTY3MjA4.YVXjhA.8Yso2FjPiYx6BDoxxLv6t5_ZuDc")
