# Discord Role Display Bot

A simple and elegant Discord bot that automatically displays user roles in a specified channel using embedded messages.

## Features

- 🎯 Channel-specific role display
- 💅 Beautiful embedded messages with user avatar
- 📝 Bullet-point list of user roles
- 🧹 Auto-deletion of messages after 4 minutes
- 🎨 Clean and modern UI design

## Setup

1. Clone this repository
```bash
git clone https://github.com/yourusername/discord-role-display-bot.git
cd discord-role-display-bot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure the bot
   - Create a new Discord application at [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a bot for your application and copy the bot token
   - Replace the token in `bot.py` with your bot token
   - Update the `CHANNEL_ID` in `bot.py` with your desired channel ID

4. Run the bot
```bash
python bot.py
```

## Configuration

- `CHANNEL_ID`: The ID of the channel where the bot should display roles
- Bot Token: Your Discord bot token (keep this secret!)
- Message deletion timer: Currently set to 4 minutes (can be modified in the code)

## Requirements

- Python 3.8 or higher
- discord.py 2.3.2
- Discord bot token
- Server with required bot permissions:
  - Read Messages
  - Send Messages
  - Manage Messages (for deletion)
  - Read Message History

## Security Note

⚠️ Never commit your bot token to GitHub. Always keep it private and secure.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
