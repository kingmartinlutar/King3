# King3
# Telegram Bot

This Telegram bot allows users to access restricted content from private channels, groups, or protected media using authenticated user sessions.

## Features
- Retrieve posts from private channels/groups
- Download protected media
- Secure session management

## Setup
1. Clone the repository
2. Create a `.env` file with your `API_ID`, `API_HASH`, `BOT_TOKEN`, and `ADMINS`
3. Build and run the Docker container

```bash
docker build -t telegram_bot .
docker run -d --name telegram_bot -p 5000:5000 telegram_bot
