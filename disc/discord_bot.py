# TODO 미완성
# disc developer portal : https://discord.com/developers/applications
# API reference : https://discordpy-ko.github.io/api.html

import discord
from discord.ext import commands

token = 'OTc0MzI0NTg4NzI3MTExNzIw.GqyADY.TTWA_LphfJuDB6FrdHWzy-nDLfDQxlsRGfWp1A'

# discord Client class를 생성합니다.

bot = commands.Bot(command_prefix='!')

# event decorator를 설정하고 on_message function을 할당해줍니다.
@bot.event
async def on_message(message):
    # message란 discord 채널에 올라오는 모든 message를 의미합니다.
    # 따라서 bot이 보낸 message도 포함이되죠.
    # 아래 조건은 message의 author가 bot(=client.user)이라면 그냥 return으로 무시하라는 뜻입니다.
    print('on_message=' + message.content)

    # message를 보낸 사람이 bot이 아니라면 message가 hello로 시작하는 경우 채널에 Hello!라는 글자를 보내라는 뜻입니다.
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


# 위에서 설정한 client class를 token으로 인증하여 실행합니다.
bot.run(token)
