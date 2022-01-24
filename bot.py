# Import libarys
import nextcord
from nextcord.ext import commands
import config
import os
bot = commands.Bot(command_prefix = "!")

# Once bot is turned on. (on ready)
@bot.event
async def on_ready():
    print("Bot is ready!")


# Create command hello which returns hello there.
@bot.command()
async def hello(ctx):
    # Sends hello there to channel the commands was executed in
    await ctx.send('Hello there!')


# Create command load, which loads the specific cog
@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    # Loads the cog specified in the message.
    bot.load_extension(f'cogs.{extension}')
    # Sends message to channel command was executed in. 'Load cog {cog}'
    await ctx.send(f'Loaded cog {extension}')



# Load all cogs
for filename in os.listdir('./cogs/'):
    # Checks to see if filename ends with .py
    if filename.endswith('.py'):
        # Loads the cog
        bot.load_extension(f'cogs.{filename[:-3]}')
        # Prints cogs loaded to console
        print(f'Loaded cog: {filename[:-3]}\n')
    else:
        # Prints error message to console if can't load cog
        print(f'Failed to load cog: {filename[:-3]}\n')

# Login to bot
bot.run(config.TOKEN)