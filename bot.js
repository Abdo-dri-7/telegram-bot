const TelegramBot = require('node-telegram-bot-api');

// حط التوكن ديالك هنا
const token = '8837865586:AAHkt6SceG-jRWlOSjmADzuFdS6JWNAR7Y4';

const bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, "👋 سلام! البوت خدام دابا");
});

bot.on('message', (msg) => {
  if (msg.text !== '/start') {
    bot.sendMessage(msg.chat.id, "وصلني: " + msg.text);
  }
});

