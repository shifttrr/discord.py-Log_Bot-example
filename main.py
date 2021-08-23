#main.pyで動かしたいという欲張りな人のためにです
#ほかの機能も取り込んでLogを取りたい！のであればlog.pyをCogで動かしましょう

import discord
from discord.ext import commands
from discord import Embed
import datetime

#Botのクライアント設定
bot = commands.Bot(command_prefix="")
#一応ヘルプ消すやつ
bot.remove_command("help")

#ここにチャンネルIDを指定してね(ログを投稿するチャンネル)
log_channel_id = id

@bot.event
async def on_ready():
    print('READY')

@bot.event
async def on_message(message):
    channel = bot.get_channel(log_channel_id)
    if message.author.id == bot.user.id:
        None
        return

    #DMのメッセージを取得
    if not message.guild:
        embed=discord.Embed(
            color=0x00ff00,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='内容',value=f'{message.content}\n\n({message.id})',inline=False)
        embed.add_field(name='チャンネル',value=f'DM ({message.channel.id})',inline=False)
        embed.add_field(name='URL',value=f'[Jump](https://discord.com/channels/@me/{message.channel.id}/{message.id})',inline=False)
        embed.set_author(name=f"{message.author} ({message.author.id}) の新規メッセージ (DM)", icon_url=message.author.avatar_url)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await channel.send(embed=embed)
        
        #サーバーのメッセージを取得
    else:
        embed=discord.Embed(
            color=0x00ff00,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='内容',value=f'{message.content}\n\n({message.id})',inline=False)
        embed.add_field(name='サーバー',value=f'{message.guild} ({message.guild.id})',inline=False)
        embed.add_field(name='チャンネル',value=f'{message.channel.mention} ({message.channel.id})',inline=False)
        embed.add_field(name='URL',value=f'[Jump](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})',inline=False)
        embed.set_author(name=f"{message.author} ({message.author.id}) の新規メッセージ", icon_url=message.author.avatar_url)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await channel.send(embed=embed)

@bot.event
async def on_message_edit(message_before, message_after):
    channel = bot.get_channel(log_channel_id)
    if message_before.author.id == bot.user.id:
        None
        return

    #DMのメッセージ編集
    if not message_before.guild:
        embed = discord.Embed(
            color=0x0000ff,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='内容',value=f'**編集前**\n{message_before.content}\n**編集後**\n{message_after.content}\n\n({message_after.id})',inline=False)
        embed.add_field(name='チャンネル',value=f'DM ({message_after.channel.id})',inline=False)
        embed.add_field(name='URL',value=f'[Jump](https://discord.com/channels/@me/{message_after.channel.id}/{message_after.id})',inline=False)
        embed.set_author(name=f"{message_after.author} ({message_after.author.id}) がメッセージを編集 (DM)", icon_url=message_after.author.avatar_url)
        if len(message_after.attachments) > 0:
            embed.set_image(url = message_after.attachments[0].url)
        await channel.send(embed=embed)

    #サーバーのメッセージ編集
    else:
        embed = discord.Embed(
            color=0x0000ff,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='内容',value=f'**編集前**\n{message_before.content}\n**編集後**\n{message_after.content}\n\n({message_after.id})',inline=False)
        embed.add_field(name='サーバー',value=f'{message_after.guild} ({message_after.guild.id})',inline=False)
        embed.add_field(name='チャンネル',value=f'{message_after.channel.mention} ({message_after.channel.id})',inline=False)
        embed.add_field(name='URL',value=f'[Jump](https://discord.com/channels/{message_after.guild.id}/{message_after.channel.id}/{message_after.id})',inline=False)
        embed.set_author(name=f"{message_after.author} ({message_after.author.id}) がメッセージを編集", icon_url=message_after.author.avatar_url)
        if len(message_after.attachments) > 0:
            embed.set_image(url = message_after.attachments[0].url)
        await channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(log_channel_id)
    if message.author.id == bot.user.id:
        None
        return

    #DMのメッセージ編集
    if not message.guild:
        embed = discord.Embed(
            color=0xff0000,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='内容',value=f'{message.content}\n\n({message.id})',inline=False)
        embed.add_field(name='チャンネル',value=f'DM ({message.channel.id})',inline=False)
        embed.add_field(name='URL',value=f'[Jump](https://discord.com/channels/@me/{message.channel.id}/{message.id})',inline=False)
        embed.set_author(name=f"{message.author} ({message.author.id}) がメッセージを削除 (DM)", icon_url=message.author.avatar_url)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await channel.send(embed=embed)

    #サーバーのメッセージ編集
    else:
        embed = discord.Embed(
            color=0xff0000,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='内容',value=f'{message.content}\n\n({message.id})',inline=False)
        embed.add_field(name='サーバー',value=f'{message.guild} ({message.guild.id})',inline=False)
        embed.add_field(name='チャンネル',value=f'{message.channel.mention} ({message.channel.id})',inline=False)
        embed.add_field(name='URL',value=f'[Jump](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})',inline=False)
        embed.set_author(name=f"{message.author} ({message.author.id}) がメッセージを編集", icon_url=message.author.avatar_url)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await channel.send(embed=embed)

@bot.event
async def on_voice_state_update(member, before, after):
    channel = bot.get_channel(log_channel_id)

    #ボイスチャンネル参加を取得
    if before.channel is None and after.channel is not None: 
        embed = discord.Embed(
            color=0x0000ff,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='サーバー',value=f'{member.guild} ({member.guild.id})',inline=False)
        embed.add_field(name='チャンネル',value=f'{after.channel.mention} ({after.channel.id})',inline=False)
        embed.set_author(name=f"{member} ({member.id}) がボイスチャンネルに参加", icon_url=member.avatar_url)
        await channel.send(embed=embed)
        return

    #ボイスチャンネル離脱を取得
    if after.channel is None and before.channel is not None: 
        embed = discord.Embed(
            color=0xff0000,
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name='サーバー',value=f'{member.guild} ({member.guild.id})',inline=False)
        embed.add_field(name='チャンネル',value=f'{before.channel.mention} ({before.channel.id})',inline=False)
        embed.set_author(name=f"{member} ({member.id}) かボイスチャンネルから離脱", icon_url=member.avatar_url)
        await channel.send(embed=embed)
        return

bot.run("TOKEN")