#Log.py それ以外の名前にしたい場合は12行の"log"の部分、一番最後の"log"の部分を変えてください

import discord
from discord.ext import commands
from discord import Embed
import datetime

##ここにチャンネルIDを指定してね(ログを投稿するチャンネル)
log_channel_id = id

class log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('log.py READY')
    

    @commands.Cog.listener()
    async def on_message(self,message):
        channel = self.bot.get_channel(log_channel_id)
        if message.author.id == self.bot.user.id:
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

    @commands.Cog.listener()
    async def on_message_edit(self,message_before, message_after):
        channel = self.bot.get_channel(log_channel_id)
        if message_before.author.id == self.bot.user.id:
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

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        channel = self.bot.get_channel(log_channel_id)
        if message.author.id == self.bot.user.id:
            None
            return

        #DMのメッセージ削除
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
            embed.set_author(name=f"{message.author} ({message.author.id}) がメッセージを削除", icon_url=message.author.avatar_url)
            if len(message.attachments) > 0:
                embed.set_image(url = message.attachments[0].url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self,member, before, after):
        channel = self.bot.get_channel(log_channel_id)

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


def setup(bot):
    return bot.add_cog(log(bot))