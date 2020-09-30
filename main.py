import discord
from discord.ext import commands
# Import the keep alive file
import keep_alive
import os
import replit
import requests


def get_prefix(client, message):

    prefixes = [
        '+'
    ]  # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['+']  # Only allow '+' as a prefix when in DMs

    # Allow users to @mention the bot instead of using a prefix when using a command.
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(
    # Create a new bot
    command_prefix=get_prefix,  # Set the prefix
    description='A moderation and fun bot',  # Set a description for the bot
    owner_id=612469019173453848,  # Your unique User ID
    case_insensitive=True  # Make the commands case insensitive
)

# case_insensitive=True is used as the commands are case sensitive by default

cogs = ['cogs.fun', 'cogs.basic', 'cogs.embed', 'cogs.moderation']

#cogs to be loaded later, 'cogs.userinfo' and 'cogs.music'

@bot.event
async def on_ready():
    replit.clear()
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    bot.remove_command('help')
    # Removes the help command
    # Make sure to do this before loading the cogs
    for cog in cogs:
        bot.load_extension(cog)
    return
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"28 servers!"))


@bot.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(
        f"Set the slowmode delay in this channel to {seconds} seconds!")


#@bot.command(name='userinfo', description='gets info on a user')
#async def getname(ctx, member: discord.Member):

#    await ctx.send(f'User name: {member.name}, id: {member.id}')
#
#    with requests.get(member.avatar_url_as(format='png')) as r:
#        img_data = r.content
#    with open(f'{member.name}.png', 'wb') as f:
#        f.write(img_data)


# Start the server
keep_alive.keep_alive()

# Finally, login the bot
bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
