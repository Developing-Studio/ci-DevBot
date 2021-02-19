from datetime import datetime
import discord
from discord.ext import commands
import os
from pretty_help import PrettyHelp


start_time = datetime.utcnow()


description = """
DevBot - A Bot for Devhub
"""
bot = commands.Bot(
    command_prefix=["!", ">", "."],
    owner_ids={747451011484090479, 727365670395838626},
    # If you remove the above line then I kick bot.
    intents=discord.Intents.all(),
    help_command=PrettyHelp(),
    description=description,
    case_insensitive=True,
    start_time=start_time,
)


@bot.event
async def on_ready():
    print("Bot is ready")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

"""
Joins and Leaves
"""


@bot.event
async def on_member_join(member):
    guild = member.guild
    channel_only = bot.get_channel(792605024206323713)
    embed = discord.Embed(
        title=f":wave: {member.name} Joined {guild.name}",
        description=f"Welcome to {guild.name}",
        color=0x00FFFF,
    )
    embed.set_thumbnail(url=member.avatar_url)
    await channel_only.send(f"{member.mention}", embed=embed)


@bot.event
async def on_member_remove(member):
    guild = member.guild
    channel_only = bot.get_channel(792605024206323713)
    embed = discord.Embed(
        title=f":wave: {member.name} Left {guild.name}",
        description=f"We hope you come back to {guild.name}",
        color=0x00FFFF,
    )
    embed.set_thumbnail(url=member.avatar_url)
    await channel_only.send(f"{member.mention}", embed=embed)


bot.load_extension("jishaku")


token = os.environ.get("TOKEN")


bot.run(f"{token}")
