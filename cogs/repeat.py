# Libarys
import nextcord
from nextcord.ext import commands

# Creates class called repeat
class repeat(commands.Cog):
    # Init a function called init to init our bot
    def __init__(self, bot):
        self.bot = bot

    # Create command called repeat with the argument message.
    # Note that we dont use @bot.command() we now use @commands.command()
    @commands.command()
    async def repeat(self, ctx, message=None):
        # If there is no argument sent by the user. We send a error message
        if message is None:
            # Sends message to channel the command was executed in. 'You need to put a message for me to resend'
            await ctx.send('You need to put a message for me to resend.')
        # If there is a message
        else:
            # Send message to channel the command was executed in. 'You said: {msg}'
            await ctx.send(f'You said: {message}')

# Creates a function called setup
def setup(bot):
    # Adds the cog to the bot index. 
    bot.add_cog(repeat(bot))