import json
from random import random
import random

import discord
from discord.ext import commands


# Intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

# Activation des intents pour le contenu des messages, les serveurs et les membres
intents.messages = True
intents.guilds = True
intents.members = True

with open("joke.json", "r", encoding="utf-8") as file:
    blagues = json.load(file)


# Fonction "on_ready" pour confirmer la bonne connexion du bot sur votre serveur
@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est bien connecté !")


# Événement de message
@bot.command()
async def tg(ctx):
    await ctx.send("t'es grraou @Alister")
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def pong(ctx):
    await ctx.send('ping')
@bot.command()
async def membres(ctx):
    guild = ctx.guild  # Récupère le serveur depuis le contexte
    members = guild.members  # Récupère la liste des membres du serveur

    # Envoie la liste des membres dans le canal où la commande a été exécutée
    await ctx.send(f"Liste des membres du serveur {guild.name} :")
    for member in guild.members:
        await ctx.send(f"- {member.display_name}")

@bot.command()
async def joke(ctx):
    # Choisir une blague aléatoire depuis la liste
    blague = random.choice(blagues)
    setup = blague["setup"]
    punchline = blague["punchline"]
    await ctx.send(f"**Blague** : \n{setup}\n*{punchline}*")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore les messages du bot lui-même

    content = message.content.lower()

    # Détection de mots-clés et ajout de réactions
    if "bonjour" in content:
        await message.add_reaction("👋")  # Ajoute un emoji de salutation
    elif "au revoir" in content:
        await message.add_reaction("👋")  # Ajoute un emoji de salutation aussi
    if "quoi" in content:
        await message.channel.send("COUBEH !!!")
    if "la plus belle" in content:
        await message.author.ban(reason="Utilisation du mot interdit 'la plus belle'")
        await message.channel.send(f"{message.author.mention} a été banni pour avoir PRONONCÉ LE MOT INETERDIT 'la plus belle'.")
        await bot.process_commands(message)
    else:
        # Si le message ne contient pas "la plus belle", traiter les autres commandes normalement
        await bot.process_commands(message)


@bot.command()
async def welcome(ctx):
    # Récupérer le pseudo de l'auteur de la commande
    author_name = ctx.author.display_name
    # Envoyer le message de bienvenue personnalisé dans le canal où la commande a été exécutée
    await ctx.send(f"Salut {author_name} mon ptit bg bienvenue sur le serveur !")

    # Fonction "on_member_join" pour envoyer le message de bienvenue lorsqu'un nouvel utilisateur rejoint le serveur
@bot.event
async def on_member_join(member):
    # Envoyer le message de bienvenue dans le canal de bienvenue
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"Salut {member.display_name} mon ptit bg bienvenue sur le serveur !")


@bot.command()
async def cmd(ctx):
    # Crée une liste des commandes disponibles
    commands_list = [
        "!ping: Répond par 'pong'.",
        "!pong: Répond par 'ping'.",
        "!membres: Affiche la liste des membres du serveur.",
        "!joke: Envoie une blague aléatoire.",
        "!welcome: Envoie un message de bienvenue personnalisé."
    ]

    # Envoie la liste des commandes dans le canal où la commande a été exécutée
    await ctx.send("Liste des commandes disponibles :\n" + "\n".join(commands_list))


bot.run("")
