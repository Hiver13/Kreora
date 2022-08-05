active = False
import time
import random
import discord
import requests
from discord.ext import commands
client = commands.Bot(command_prefix = ".", self_bot = True)
client.remove_command("help")


@client.event
async def on_ready():
    print("▒█░▄▀ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▀█ ▒█▀▀█ ░█▀▀█ 　 ▒█▀▀█ ▒█▀▀▀ ▀▀█▀▀ ░█▀▀█ 　 ▄█░ ░ █▀▀█\n▒█▀▄░ ▒█▄▄▀ ▒█▀▀▀ ▒█░░▒█ ▒█▄▄▀ ▒█▄▄█ 　 ▒█▀▀▄ ▒█▀▀▀ ░▒█░░ ▒█▄▄█ 　 ░█░ ▄ █▄▀█\n▒█░▒█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█ 　 ▒█▄▄█ ▒█▄▄▄ ░▒█░░ ▒█░▒█ 　 ▄█▄ █ █▄▄█")

@client.command()
async def help(ctx):
    await ctx.send("**Kreora Beta **\n`.say(текст) - отправляет сообщение`\n`.spam(количество)(текст) - спамит сообщением`\n`.popit отправляет попыт`\n`.ben(вопрос) - спрашивает бена`\n`.anekdot - расказывает анекдот `")

@client.command()
async def say(ctx, *, text):
    await ctx.send(text)

@client.command()
async def spam(ctx, kv, *, text):
    while int(kv) !=0:
        await ctx.send(text)
        kv = int(kv)-1

@client.command()
async def popit(ctx):
   await ctx.send("||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||\n||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||\n||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||\n||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||\n||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||")


@client.command()
async def ben(ctx, *, text):
    ballik = random.randint(1, 4)
    if ballik == 1:
        await ctx.send("Да")
    if ballik == 2:
        await ctx.send("Угрх..")
    if ballik == 3:
        await ctx.send("Нет")
    if ballik == 4:
        await ctx.send("Хо-хо-хо")


@client.command()
async def anekdot(ctx):
    ballik = ["А вы замечали, что когда к вам обращаются с фразой (Нам надо поговорить), вам-то это как раз совершенно не надо?", "Считать, что современные люди заложники своих гаджетов это большое преувеличение.Они заложники аккумуляторов своих гаджетов.", "Доктор, полгода назад я развелся с женой. Прибавил в весе 30 кило. — Это же элементарно лечится! Просто перестаньте уже праздновать.", "Покурил сигареты Президент, но президентом не стал. Выпил водку Парламент, но в парламенте не заседаю. И только когда пью пиво Козел, чувствую — действует…", "Дед, а у вас тут куда вечером сходить-то можно? — В ведро.", "— Какая у больного температура? — Нормальная, комнатная, +18 градусов...", "— А существуют таблетки от голода? — Да, котлеты называются! ", "Хочу себе свой портрет Дориана Грея, только чтобы он тупил вместо меня.", "Все мы когда-то были друг другу чужими, а потом нет, а потом снова да."]
    await ctx.send(random.choice(ballik))

client.run("Твой токен", bot = False)
