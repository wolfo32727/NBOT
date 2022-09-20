import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="-", intents=intents)
client.remove_command("help")

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="Jesteśmy za biedni by zrobić komende help D:")
    embed.add_field(name="Dlatego mamy free robux", value="Strona: https://wolfo32727.github.io/Wolfo", inline=True)
    embed.set_footer(text="NA CO SIĘ KURWA GAPISZ")
    await ctx.send(embed=embed)

@client.command()
async def setStatus(ctx, *, game):
    await client.change_presence(activity=discord.Game(name=game))
    await ctx.channel.send(f"Ustawiono grę na {game}")


client.run("MTAyMTQ5MDQ2Mzg0NjQzNjkxNg.GFtVPs.iE0NlocqwLf-LTU-LzHN7_JIhyTHeAHkWr9ynk")