"""
This module contains a Telegram bot that handles various commands 
related to product changes and wishlist management.
"""

import telebot
from bot_config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start", "help"])
def welcome(message):
    """
    Handles the /start and /help commands.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    if message.text == "/start":
        bot.send_message(
            message.chat.id, f"Welcome to the bot {message.from_user.first_name}!")
        bot.send_message(message.chat.id, "use the command /help to get help")
    if message.text == "/help":
        bot.send_message(
            message.chat.id, "You can use the following commands:")
        bot.send_message(
            message.chat.id, "all_changes - List all the changes during today")
        bot.send_message(
            message.chat.id, "new_products - List the new products added today")
        bot.send_message(
            message.chat.id, "remove_products - List the removed products today")
        bot.send_message(
            message.chat.id, "change_products - List the products changed today")
        bot.send_message(
            message.chat.id, "add_wishlist - Add a product to the wishlist")
        bot.send_message(
            message.chat.id, "remove_wishlist - Remove a product from the wishlist")


@bot.message_handler(regexp="all_changes")
def reply_all_changes(message):
    """
    Replies with a list of all changes during today.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(message, text="List all the changes during today")


@bot.message_handler(regexp="new_products")
def reply_new_products(message):
    """
    Replies with a list of new products added today.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(message, text="List the new products added today")


@bot.message_handler(regexp="remove_products")
def reply_remove_products(message):
    """
    Replies with a list of removed products today.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(message, text="List the removed products today")


@bot.message_handler(regexp="change_products")
def reply_change_products(message):
    """
    Replies with a list of products changed today.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(message, text="List the products changed today")


@bot.message_handler(regexp="add_wishlist")
def reply_add_wishlist(message):
    """
    Adds a product to the wishlist.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(
        message, text=f"Adding the product {message.text} to the wishlist")


@bot.message_handler(regexp="remove_wishlist")
def reply_remove_wishlist(message):
    """
    Removes a product from the wishlist.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(
        message, text=f"Removing the product {message.text} from the wishlist")


bot.infinity_polling()
