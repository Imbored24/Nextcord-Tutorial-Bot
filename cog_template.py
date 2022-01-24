#This is a quick way for you to be able to create a cog without having to write that boring starting code all the time.

#Libarys
import nextcord
from nextcord.ext import commands

# Creates a class called {name of command} replace nameofcommand to the name of your file.
class nameofcommand(commands.Cog):
    # Creates the init functions to init our bot
    def __init__(self, bot):
        # Sets self.bot to use bot
        self.bot = bot

    # Creates a command called {commmand name}
    # Keep in mind we dont use bot.commands() in cogs. We use commands.command()
    # Replace {command name} to the name of the command you want to make.
    @commands.command()
    # If you would like a permission added to your command. Then uncomment the line below. Replace permission with the permission required.
    #@commands.has_permissions(permission=True)
    async def commandname(self, ctx):
        # Sends message to the channel the command was executed in. 'Your message'.
        # Replace below to what you want / need.
        await ctx.send("Your message.")

# Creates a function called setup
def setup(bot):
    # Adds the cog to the bot index.
    bot.add_cog(nameofcommand(bot))