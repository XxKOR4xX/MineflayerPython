from javascript import require, On, Once, AsyncTask, once, off

# Import the javascript libraries
mineflayer = require("mineflayer")

# Create bot with basic parameters
bot = mineflayer.createBot(
    {"username": "simple-bot", "host": "Y2R9.aternos.me", "port": 46278, "version": "1.19.4", "hideErrors": False}
)

# Login event required for bot
@On(bot, "login")
def login(this):
    pass
