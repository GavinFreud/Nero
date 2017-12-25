import Discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~')
startup_exts = ['commands','voice']

@bot.event
async def on_ready():
    print('logging in')

if __name__ == '__main__':
    for ext in startup_exts:
        try:
            bot.load_extension(ext)
        except Exception as e:
            excep = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load {}\n{}'.format(ext, excep))
    bot.run(Mzk0NjiMwMzUwMjA0MTc0MzM3.DSHHtg.M5N4Bt8WZvOyOeat1oy0BGY0DEI)
