import asyncio
import discord

async def music_info(player, bot, server):
    embed = discord.Embed()
    m, s = divmod(player.duration, 60)
    embed.title = 'Music'
    embed.add_field(name="Title", value = player.title, inline = True)
    embed.add_field(name="Duration", value=str("{}:{}".format(m, s)), inline = True)
    embed.color = discord.Color.dark_purple()

    channel = await find_text_channel("Nero bullshit", server, bot)
    await bot.send_message(channel, "", embed=embed)

async def find_text_channel(name, server, bot):
    channels = server.channels
    for channel in channels:
        if(channel.type) == 'text' and channel.name = name:
            return channel
    return await bot.create_channel(name = name, server = server, type = 'text')

async def find_voice_channel(name, server, bot):
    channels = server.channels
    for channel in channels:
        if(channel.type) == 'voice' and channel.name = name:
            return channel
    return await bot.create_channel(name=name, server=server, type='voice')



