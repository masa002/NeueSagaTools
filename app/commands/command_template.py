# commands/command_template.py
import discord
from discord.ext import commands

# コマンドの設定情報
COMMAND_NAME = "command_name"  # 実際のコマンド名を指定
COMMAND_DESCRIPTION = "このコマンドの説明をここに記述します。"
COMMAND_USAGE = f"`/{COMMAND_NAME} パラメータ1 パラメータ2 ...`"
COMMAND_EXAMPLE = f"/{COMMAND_NAME} 例1 例2"
COMMAND_RESULT_DESCRIPTION = "コマンドの結果がどのように表示されるか、または期待される動作をここに記述します。"

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
    embed.add_field(
        name="結果の説明",
        value=COMMAND_RESULT_DESCRIPTION,
        inline=False
    )
    return embed

@commands.command(name=COMMAND_NAME)
async def command_name(ctx, *args):
    """
    コマンドの実際の処理を行う関数。
    """
    # 引数が空の場合はヘルプメッセージを表示
    if not args:
        embed = generate_help_embed()
        await ctx.send(embed=embed)
        return

    try:
        # コマンドの処理をここに記述します
        # 例: await ctx.send(f"パラメータ: {args}")
        await ctx.send("コマンドの処理結果をここに送信")
    
    except Exception as e:
        await ctx.send(f"⚠️ エラーが発生しました: {str(e)}")

# Botにこのコマンドを追加するためのセットアップ関数
def setup(bot):
    bot.add_command(command_name)
