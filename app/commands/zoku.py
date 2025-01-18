# commands/zoku.py
import discord
from discord.ext import commands
import csv
import math

# コマンドの設定情報
COMMAND_NAME = "zoku"  # 実際のコマンド名を指定
COMMAND_DESCRIPTION = "賊軍拠点の占領値割　計算コマンドです"
COMMAND_USAGE = f"`/{COMMAND_NAME} パラメータ1(星域名 or 星域ランク) パラメータ2(人数)`"
COMMAND_EXAMPLE = f"/{COMMAND_NAME} カストロプ 4"

MISSTAKE_RANGE = 50

def generate_help_embed():
    """
    コマンド用のヘルプメッセージを生成する。
    """
    embed = discord.Embed(
        title=f"📘 /{COMMAND_NAME} コマンドの使い方",
        description=COMMAND_DESCRIPTION,
        color=discord.Color.blue()
    )
    embed.add_field(
        name="使い方",
        value=f"{COMMAND_USAGE}\n\n**例**: {COMMAND_EXAMPLE}",
        inline=False
    )
    return embed

@commands.command(name=COMMAND_NAME)
async def command_name(ctx, *args):
    """
    コマンドの実際の処理を行う関数。
    """

    if not args:
        embed = generate_help_embed()
        await ctx.send(embed=embed)
        return

    try:
        with open('./app/res/zoku.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        if not args[1].isdecimal():
            await ctx.send(f"⚠️ 割る数の型が不正です")
            return
        if args[1] == "0":
            await ctx.send(f"⚠️ 0で割ることはできません")
            return

        if args[0].isdecimal():
            data = [row for row in data if row['AreaRank'] == args[0]]
        else:
            data = [row for row in data if row['AreaName'] == args[0]]
        
        hp_list = [int(item['BaseHp']) for item in data]
        base_rank_list = [item['BaseRank'] for item in data]
        div_hp_list = [math.ceil(item / int(args[1]) / 100) * 100 for item in hp_list]

        embed = discord.Embed(
            title="🧮 計算結果",
            color=discord.Color.green()
        )

        text = ''
        for i, rank in enumerate(base_rank_list):
            text += f'{rank}: {div_hp_list[i]}\n'

        embed.add_field(name=text, value='\u200b')

        if hp_list[0] / (div_hp_list[-1] + MISSTAKE_RANGE) > int(args[1]) - 1:
            embed.add_field(name=f'ALL: {div_hp_list[-1]}', value='\u200b', inline=False)

        embed.set_footer(text="Created by masakk", icon_url="https://cdn.discordapp.com/avatars/300600992582467585/8b642269d5e5821d7ebd583057c4f841")

        await ctx.send(embed=embed)
    
    except Exception as e:
        await ctx.send(f"⚠️ エラーが発生しました: {e}")

# Botにこのコマンドを追加するためのセットアップ関数
def setup(bot):
    bot.add_command(command_name)
