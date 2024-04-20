#
#  _   _  ___ _____ _____ _   _ _____ ____  _____    _    _   _____  _    ____  
# | \ | |/ _ \_   _|_   _| | | | ____|  _ \| ____|  / \  | | |_   _|/ \  |  _ \ 
# |  \| | | | || |   | | | |_| |  _| | |_) |  _|   / _ \ | |   | | / _ \ | |_) |
# | |\  | |_| || |   | | |  _  | |___|  _ <| |___ / ___ \| |___| |/ ___ \|  _ < 
# |_| \_|\___/ |_|   |_| |_| |_|_____|_| \_\_____/_/   \_\_____|_/_/   \_\_| \_\
# 

from redbot.core import commands
from discord import Embed, User
import random

class HowCracked(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def howcracked(self, ctx, user: User = None):
        """
        Rate the cracked level of a user or yourself.
        """
        # Define cool power levels and emojis
        cool_power_levels = [
            "Ultra Mega Super Cracked",
            "Super Duper Cracked",
            "Mega Cracked",
            "Cracked",
            "Kinda Cracked",
            "Not So Cracked",
            "Un-Cracked",
            "Butt-Crack-ed",
            "On-Crack",
        ]

        emojis = ["💯", "😎", "🔥", "🤯", "👀"]

        cool_ability_levels = [
            "Ultra Mega Super Charismatic",
            "Super Duper Strong",
            "Mega Intelligent",
            "Mildly Psychic",
            "Slightly Telekinetic",
            "Not So Nimble",
            "Un-coordinated",
            "Butt-Smooth Talker",
            "Crack-Head",
            "Intellect",
            "Rizz",
        ]
        
        # Define gifs for each power level
        gifs = {
            "Ultra Mega Super Cracked": "https://cdn.discordapp.com/attachments/1170989523895865424/1231326884495626391/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f416c796550784f326367616f65513d3d2d313335323730343938352e3137363939386662303861383332333039.gif?ex=66368d86&is=66241886&hm=bd2e0f5356674cc86e8bdd2756bdab54dd57606653e5d0a015de5424e5a1986f&",
            "Super Duper Cracked": "https://cdn.discordapp.com/attachments/1170989523895865424/1231324806297682059/monkey-d-luffy-straw-hat-luffy.gif?ex=66368b96&is=66241696&hm=09496efa42a3abd479ae6f3184fbe0abaec57e01a9550f9a7e96349b368a8b51&",
            "Mega Cracked": "https://cdn.discordapp.com/attachments/1170989523895865424/1231324623891861565/kermit-dragonballz.gif?ex=66368b6b&is=6624166b&hm=c47b1379fb442ed31ab65787d64abf14fdb9285e0b2b65cae9a0f4cefcf6b97d&",
            "Cracked": "https://cdn.discordapp.com/attachments/1170989523895865424/1231324438759473223/power-up-strong.gif?ex=66368b3f&is=6624163f&hm=fd0ec8e77be9faae5b64e6c6cbe0af1234068d935991b3aa1b27cf4cc54cb678&",
            "Kinda Cracked": "https://cdn.discordapp.com/attachments/1170989523895865424/1231323970784202842/dont-know-why-i-was-reminded-of-those-10-year-old-kids-who-studies-coding-weight.gif?ex=66368acf&is=662415cf&hm=67af041bf0de0f0cfbda84f0a33d5a2ef971833ada5b22bda5ea8848c8c9b0e0&",
            "Not So Cracked": "https://cdn.discordapp.com/attachments/1170989523895865424/1231323783676170370/try-to-get-up-zayto.gif?ex=66368aa2&is=662415a2&hm=a9a7c4f273fbf2ea4e51018df15bd7a8ee33747a1d616de3b096ef708951222e&",
            "Un-Cracked": "https://cdn.discordapp.com/attachments/1170989523895865424/1231323312471146506/duct-tape-this-is-the-end.gif?ex=66368a32&is=66241532&hm=5b1b732ff4c8eedc413cafea340ba90aae625dba56b751535eb913e26cbb71e4&",
            "Butt-Crack-ed": "https://cdn.discordapp.com/attachments/1170989523895865424/1231322898015191040/homer-simpson.gif?ex=663689cf&is=662414cf&hm=94ebbbb21c9a16cfea87d5e05b112d056bfec370dacb345413b504c99802106e&",
            "On-Crack": "https://cdn.discordapp.com/attachments/1170989523895865424/1231323348445692004/IMG_2579.gif?ex=662566bb&is=6624153b&hm=82eaa02dfd5d734e577a5d5c38c9dca571b44c3812f6660a1e0a3ea8e5ad6896&",
        }

        # Get the user to rate
        target_user = user or ctx.author

        # Generate a random cracked percentage
        cracked_percentage = random.uniform(0, 100)

        # Determine the cool power level based on the percentage
        power_level = None
        if cracked_percentage < 7:
            power_level = "On-Crack"
        elif cracked_percentage < 25:
            power_level = "Not So Cracked"
        elif cracked_percentage < 50:
            power_level = "Kinda Cracked"
        elif cracked_percentage < 75:
            power_level = "Cracked"
        elif cracked_percentage < 90:
            power_level = "Mega Cracked"
        elif cracked_percentage < 97:
            power_level = "Super Duper Cracked"
        else:
            power_level = "Ultra Mega Super Cracked"

        # Determine the cool ability level based on the percentage
        ability_level = None
        if cracked_percentage < 7:
            ability_level = "Crack-Head"
        elif cracked_percentage < 25:
            ability_level = "Un-coordinated"
        elif cracked_percentage < 50:
            ability_level = "Not So Nimble"
        elif cracked_percentage < 75:
            ability_level = "Mildly Psychic"
        elif cracked_percentage < 90:
            ability_level = "Slightly Telekinetic"
        elif cracked_percentage < 97:
            ability_level = "Mega Intelligent"
        else:
            ability_level = "Ultra Mega Super Charismatic"

        # Build the embed
        embed = Embed(title=f"How Cracked is {target_user.name}?", color=0x00ff00)
        embed.description = f"{target_user.mention} is {power_level}! {cracked_percentage:.2f}% {ability_level} {random.choice(emojis)}"
        embed.set_footer(text="Powered by the Cracked-o-Meter and Goku")

        # Send the embed
        await ctx.send(embed=embed)

# Required to make the cog load
def setup(bot):
    bot.add_cog(HowCracked(bot))