import discord
from typing import Any, List

async def imageperms(message: discord.Message, args: List[str], client: discord.Client, **kwargs: Any) -> Any:
    await message.channel.send("Image perms are not available for everyone due to continued raids on this server. To obtain them, send 300 messages and DankBot will automatically give you permissions.\n\nPlease note that only messages sent after 2021\-06\-06 count.")

async def dankpod(message: discord.Message, args: List[str], client: discord.Client, **kwargs: Any) -> Any:
    await message.channel.send("DankPods is **not** and has **never** been in this server. Due to fan harassment in the past he has completely deleted his Discord account, however, he is aware about this server's existence and endorses it.")

async def patreonjoin(message: discord.Message, args: List[str], client: discord.Client, **kwargs: Any) -> Any:
    await message.channel.send("If you're confused as to why you are here despite not joining yourself, you're probably subbed to DankPods on Patreon, and have your Patreon account linked to your Discord account. Patreon automatically joins you to available Patreon-linked guilds from creators you support at the start of every month.\n\nIf you'd like to stop this from happening, sadly the only option is to unlink your Patreon account from Discord, but that way you'll lose any Patreon perks you have on other Discord guilds.")

async def advice(message: discord.Message, args: List[str], client: discord.Client, **kwargs: Any) -> Any:
    await message.channel.send("Asking for advice here? Please fill out this form:\n\n1: Location? Some things may be accessible in other parts of the world more than others, like the US.\n2: What is your budget? List what you are comfortable with spending.\n3: Do you have any source gear such as amplifiers or DACs?\n4: What environments are you using these in? Is it noisy?\n5: What other audio equipment have you had, or, more specifically, enjoyed?\n6: What genres and types of music do you listen to?\n7: Do you want headphones, IEMs, or are you okay with either?")

async def quote(message: discord.Message, args: List[str], client: discord.Client, **kwargs: Any) -> Any:
    await message.channel.send("\"If your definition of good is crap, it can be good, but then you've never heard what good sounds like.\"\n-Psal, 2018-07-02")

async def furry(message: discord.Message, args: List[str], client: discord.Client, **kwargs: Any) -> Any:
    await message.channel.send("https://media.discordapp.net/attachments/823939225123815475/847565202212126750/VRChat_1920x1080_2021-05-27_12-59-19.541.png?width=960&height=540")

category_info = {
	'name': 'faq',
	'pretty_name': 'FAQ',
	'description': 'answers to questions because people can\'t read <#821190757003034716>, and other weird quotes'
}

commands = {
	'imageperms': {
		'pretty_name': 'imageperms',
		'description': 'Explanation on image permissions',
		'permission': 'everyone',
		'cache': 'keep',
		'execute': imageperms
	},
	'isdankpodshere': {
		'pretty_name': 'isdankpodshere',
		'description': 'Explanation on DankPods not being here.',
		'permission': 'everyone',
		'cache': 'keep',
		'execute': dankpod
	},
	'patreonjoin': {
		'pretty_name': 'patreonjoin',
		'description': 'Explanation on why a user might have been automatically put in this guild.',
		'permission': 'everyone',
		'cache': 'keep',
		'execute': patreonjoin
	},
    'advice': {
        'pretty_name': 'advice',
        'description': 'Prints the advice form',
        'permission': 'everyone',
        'cache': 'keep',
        'execute': advice
    },
    'cap': {
        'pretty_name': 'cap',
        'description': 'some quote idk humble asked me (alex) for this',
        'permission': 'everyone',
        'cache': 'keep',
        'execute': quote
    },
    'isdankpodsafurry': {
        'pretty_name': 'isdankpodsafurry',
        'description': 'maybe 😳',
        'permission': 'everyone',
        'cache': 'keep',
        'execute': furry
    },

}
version_info: str = "1.1"
