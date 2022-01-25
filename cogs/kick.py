#This is a quick way for you to be able to create a cog without having to write that boring starting code all the time.

#Libarys
import nextcord
from nextcord.ext import commands

# Creates a class called {name of command} replace nameofcommand to the name of your file.
class kick(commands.Cog):
    # Creates the init functions to init our bot
    def __init__(self, bot):
        # Sets self.bot to use bot
        self.bot = bot

    # Creates a command called {commmand name}
    # Keep in mind we dont use bot.commands() in cogs. We use commands.command()
    # Replace {command name} to the name of the command you want to make.
    @commands.command()
    # If you would like a permission added to your command. Then uncomment the line below. Replace permission with the permission required.
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : nextcord.Member=None, *, reason=None):
        if member is None and reason is None:
            await ctx.send('Please mention a member or mention a reason. e.g !kick @member reason')
        else:
            await ctx.send(f'I have kicked the member {member.mention} for the reason `{reason}`')
            try:
                await member.send(f'You have been kicked from `{ctx.guild.name}` by the staff member {ctx.author.mention} for the reason `{reason}`')
            except:
                await ctx.send(f"Cannot send message to member. Because their dms are closed.")
            await member.kick(reason=reason)

# Creates a function called setup
def setup(bot):
    # Adds the cog to the bot index.
    bot.add_cog(kick(bot))