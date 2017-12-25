import discord
from discord.ext import commands
import playlist

class Voice:

    def __init__(self, bot):
        self.bot = bot
        self.voice = None
        self.player = None
        self.volume = 1.0
        self.playlist = None
        self.time_elapse = None

    @commands.command(name="queue", pass_context=True, help="add link to queue")
    async def queue_insert(self, ctx, link):


