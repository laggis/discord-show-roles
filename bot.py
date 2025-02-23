import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

CHANNEL_ID = 1262319092975800380

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message is in the specified channel
    if message.channel.id == CHANNEL_ID:
        # Get the member's roles
        roles = [role.name for role in message.author.roles if role.name != "@everyone"]
        
        # Create embed
        embed = discord.Embed(
            title="User Roles",
            color=discord.Color.blue()
        )
        
        # Add user info to embed
        embed.set_author(
            name=message.author.display_name,
            icon_url=message.author.display_avatar.url
        )
        
        if roles:
            roles_text = "\n".join([f"• {role}" for role in roles])
            embed.description = roles_text
        else:
            embed.description = "No roles assigned"
            
        embed.set_footer(text="This message will be deleted in 4 minutes")
        
        # Send embed and store the bot's message
        bot_message = await message.channel.send(embed=embed)
        
        # Delete both messages after 4 minutes
        await asyncio.sleep(240)  # 240 seconds = 4 minutes
        try:
            await message.delete()
            await bot_message.delete()
        except discord.errors.NotFound:
            pass  # Message already deleted

    await bot.process_commands(message)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
