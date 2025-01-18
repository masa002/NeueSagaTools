# main.py
import discord
from discord.ext import commands
import os
from server import server_thread

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)



# 追加のコマンドがあればここにインポートする (例: from commands.example_command import setup as example_setup)
# from commands.command_template import setup as template_setup
from commands.zoku import setup as zoku_setup


# 各コマンドのセットアップを呼び出してBotに登録
# 追加のコマンドのセットアップ (例: example_setup(bot))
# template_setup(bot)
zoku_setup(bot)

# Botトークンを設定して実行
server_thread()
bot.run(os.getenv("DISCORD_TOKEN"))
