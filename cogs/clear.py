#This is a quick way for you to be able to create a cog without having to write that boring starting code all the time.

#Libarys
import nextcord
from nextcord.ext import commands

# Creates a class called {name of command} replace nameofcommand to the name of your file.
class clear(commands.Cog):
    # Creates the init functions to init our bot
    def __init__(self, bot):
        # Sets self.bot to use bot
        self.bot = bot

    # Creates a command called {commmand name}
    # Keep in mind we dont use bot.commands() in cogs. We use commands.command()
    # Replace {command name} to the name of the command you want to make.
    @commands.command()
    # If you would like a permission added to your command. Then uncomment the line below. Replace permission with the permission required.
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number : int=None):
        # Check to see if number has been defined
        if number is None and not int:
            await ctx.send('An error has occured! You have stated the amount of messages you want to delete. Or you need to put an integer. e.g !clear 10')
        else:
            if number > 100:
                await ctx.send('The limit of messages you can delete is 100.')
            else:
                await ctx.send(f'Clearing {number} amount of messages.')
                await ctx.channel.purge(limit=number)
                await ctx.send('Messages have been cleared')

# Creates a function called setup
def setup(bot):
    # Adds the cog to the bot index.
    bot.add_cog(clear(bot))