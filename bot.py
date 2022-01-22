# Import libarys
import nextcord
from nextcord.ext import commands
import config

bot = commands.Bot(command_prefix = "!")

# Once bot is turned on. (on ready)
@bot.event
async def on_ready():
    print("Bot is ready!")

# Create command ping which returns pong
@bot.command()
async def ping(ctx):
    # Sends pong to channel the command was executed in
    await ctx.send('Pong!')


# Create command hello which returns hello there.
@bot.command()
async def hello(ctx):
    # Sends hello there to channel the commands was executed in
    await ctx.send('Hello there!')

# Login to bot
bot.run(config.TOKEN)