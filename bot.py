"""
This module contains a Telegram bot that handles various commands 
related to product changes and wishlist management.
"""

import telebot
import wishlist
from bot_config import API_TOKEN
import files_functions

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
    elif message.text == "/help":
        bot.send_message(
            message.chat.id, "You can use the following commands:")
        commands = [
            "all_changes - List all the changes during today",
            "new_products - List the new products added today",
            "remove_products - List the removed products today",
            "change_products - List the products changed today",
            "add_wishlist - Add a product to the wishlist",
            "remove_wishlist - Remove a product from the wishlist",
            "reset_wishlist - Remove all products from the wishlist"
        ]
        for command in commands:
            bot.send_message(message.chat.id, command)


@bot.message_handler(regexp="all_changes")
def reply_all_changes(message):
    """
    Replies with a list of all changes during today.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(message, text="Here it is the list of all changes:")
    bot.reply_to(message, text="Added:")
    bot.reply_to(message, text=files_functions.get_added_products())
    bot.reply_to(message, text="Removed:")
    bot.reply_to(message, text=files_functions.get_removed_products())
    bot.reply_to(message, text="Changed:")
    bot.reply_to(message, text=files_functions.get_changed_products())


@bot.message_handler(regexp="new_products")
def reply_new_products(message):
    """
    Replies with a list of new products added today.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(message, text="Here you have the new products added today:")
    bot.reply_to(message, text=files_functions.get_added_products())


@bot.message_handler(regexp="remove_products")
def reply_remove_products(message):
    """
    Replies with a list of removed products today.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(message, text="Here you have the removed products for today:")
    bot.reply_to(message, text=files_functions.get_removed_products())


@bot.message_handler(regexp="change_products")
def reply_change_products(message):
    """
    Replies with a list of products changed today.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """
    bot.reply_to(message, text="List of products changed today:")
    bot.reply_to(message, text=files_functions.get_changed_products())


@bot.message_handler(regexp="add_wishlist")
def reply_add_wishlist(message):
    """
    Adds a product to the wishlist.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """

    wishlist.add_product_to_wishlist(message.text.replace("add_wishlist ", ""))
    bot.reply_to(
        message, text=f"Adding the product {message.text} to the wishlist")


@bot.message_handler(regexp="remove_wishlist")
def reply_remove_wishlist(message):
    """
    Removes a product from the wishlist.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """

    wishlist.remove_product_from_wishlist(
        message.text.replace("remove_wishlist ", ""))
    bot.reply_to(
        message, text=f"Removing the product {message.text} from the wishlist")


@bot.message_handler(regexp="reset_wishlist")
def reply_reset_wishlist(message):
    """
    Removes all products from the wishlist.

    Args:
        message (telebot.types.Message): The message object containing the command.
    """

    wishlist.reset_wishlist()
    bot.reply_to(message, text="Resetting the wishlist")


bot.infinity_polling()
