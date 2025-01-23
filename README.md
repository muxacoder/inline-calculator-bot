# Inline Calculator Bot

Inline Calculator Bot is a Telegram bot built with aiogram 3.x that allows users to perform basic mathematical calculations in inline mode. Simply type a math expression in any chat, and the bot will evaluate it and provide the result.

---

## Features
- Perform calculations directly in inline mode.
- Supports basic math operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Lightweight and easy to set up.

---

## How It Works
1. Type @YourBot <math_expression> (e.g., `@YourBot 3+5`) in any Telegram chat.
2. The bot calculates the result and displays it in real time.
3. Select the result to send it to the chat.

---

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/inline-calculator-bot.git
   cd inline-calculator-bot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace BOT TOKEN in .env file with your Telegram bot token from [BotFather](https://t.me/botfather)
4. Run the Bot
   ```bash
   python app.py
   ```
---
## Requirements
   - Python 3.8+
   - aiogram 3.x
---
## Example usage
- Inline qeury: ```@YourBot 12/4```
- Result:
  ```bash
  12/4=3
  ```
--- 
## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.
