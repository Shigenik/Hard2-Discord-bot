import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

TOKEN = os.environ["DISCORD_TOKEN"]
ROLE_ID = int(os.environ["ROLE_ID"])

DM_MESSAGE = """Hej! Jeteś na ostatniej prostej do dołączenia do naszej gildii! Zostało tylko dołączyć na kanał ⎾💼⏌REKRUTACJA i poczekać na któregoś z adminów. Po przejściu werfikacji zostanie Ci dodana specjalna ranga. Gramy razem. Rozwijamy się razem. ⚔️ 🎉"""

@client.event
async def on_ready():
    print(f"Bot działa jako {client.user}")

@client.event
async def on_member_update(before, after):
    # Sprawdź czy dodano nową rolę
    new_roles = set(after.roles) - set(before.roles)
    for role in new_roles:
        if role.id == ROLE_ID:
            try:
                await after.send(DM_MESSAGE)
                print(f"Wysłano DM do {after.name}")
            except discord.Forbidden:
                print(f"Nie można wysłać DM do {after.name} (zablokowane)")

client.run(TOKEN)
