import discord
from discord.ext import commands
import playlist
import helper_functions

class Voice:

    def __init__(self, bot):
        self.bot = bot
        self.voice = None
        self.player = None
        self.volume = 1.0
        self.playlist = None
        self.time_elapse = None
        self.music_server = None

    @commands.command(name="queue", pass_context=True, help="add link to queue")
    async def queue_insert(self, ctx, link):
        song = link
        self.playlist.add(song)
        if not self.music_server:
            self.music_server = self.get_or_take_member_channel(ctx)
        if self.time_elapse <= 0:
            if self.playlist.current is None:
                pass
            else:
                await self.play_music(self.playlist.pop())

    async def play_music(self, link):
        trigger = self.music_server
        if trigger is None:
            await self.bot.say("Join a channel first fool")
            return
        if self.voice:
            if self.voice.channel.id != trigger.id:
                await self.voice.move_to(trigger)
        else:
            self.voice = await self.bot.join_voice_channel(trigger)
        if self.player:
            self.player.stop()
        self.player = await self.voice.create_ytdl_player(link)
        
        await helper_functions.music_info(self.player, self.bot, self.music_server.server)

        self.player.start()
        self.time_elapse = self.player.duration
        await self.queue_poll()

    async def queue_poll(self):
        while self.time_elapse > 0:
            self.time_elapse -= 1
            await asyncio.sleep(1)

        if self.playlist.current is not None:
            await self.play_music(self.playlist.pop())
            await asyncio.sleep(5)

        elif self.playlist.current is None:
            await self.voice.disconnect()
    


