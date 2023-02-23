import os

import discord
from dotenv import find_dotenv, load_dotenv

from optimal_edge.util import get_response

load_dotenv(find_dotenv())


def main():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    tree = discord.app_commands.CommandTree(client)

    # guild=discord.Object(id=XXXXX)
    @tree.command(
        name="optimaledge",
        description="Reports whether Breaking the Limit or Second Chance is superior.",
    )
    async def optimal_edge(interaction, pool: int, edge: int, limit: int):
        text = get_response(pool=pool, edge=edge, limit=limit)
        await interaction.response.send_message(text)

    @client.event
    async def on_ready():
        """Announce slash-commands"""
        # guild=discord.Object(id=XXXXX)
        await tree.sync()
        print("Ready!")

    client.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    main()
