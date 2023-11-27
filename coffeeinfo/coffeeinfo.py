from redbot.core import commands
from redbot.core import checks
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS

class CoffeeInfo(commands.Cog):
    """Cog to display server stats in an automatically updating voice channel style."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    @checks.admin()
    async def coffeeinfo(self, ctx):
        """Set up server stats in a voice channel to display human, bot, and server boost totals."""
        if ctx.invoked_subcommand is None:
            await ctx.send_help()

    @coffeeinfo.command()
    async def setup(self, ctx):
        """Set up the voice channel to display server stats (total humans, bots, and server boosts)."""
        try:
            guild = ctx.guild
            voice_channels = [await guild.create_voice_channel(f'Humans: {guild.member_count}'),
                               await guild.create_voice_channel(f'Bots: {sum(member.bot for member in guild.members)}'),
                               await guild.create_voice_channel(f'Server Boosts: {guild.premium_subscription_count}')]

            await ctx.send("Server stats have been set up in the voice channels.")
        except Exception as e:
            await ctx.send(f"An error occurred during setup: {e}")

    @coffeeinfo.command()
    async def revert(self, ctx):
        """Remove the server stats display from the voice channels."""
        try:
            guild = ctx.guild
            for channel in guild.voice_channels:
                if channel.name.startswith(('Humans:', 'Bots:', 'Server Boosts:')):
                    await channel.delete()

            await ctx.send("Server stats display has been reverted from the voice channels.")
        except Exception as e:
            await ctx.send(f"An error occurred during revert: {e}")