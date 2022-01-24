# Libarys
import nextcord
from nextcord.ext import commands

# Creates class called ping
class ping(commands.Cog):
    # Creates a function called init this inits our bot.
    def __init__(self, bot):
        self.bot = bot

    # Creates command called ping
    # Note that we dont use @bot.command() we now use @commands.command()
    @commands.command()
    async def ping(self, ctx):
        # Sends message to the channel was executed in. 'Pong!'
        await ctx.send('Pong!')


# Creates a function called setup
def setup(bot):
    # Adds the cog to the bot index. 
    bot.add_cog(ping(bot))