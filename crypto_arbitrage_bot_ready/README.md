# Crypto Arbitrage Telegram Bot

Готовый Telegram‑бот для мониторинга арбитражных возможностей (KuCoin, Bybit, MEXC).

## Быстрый старт

1. Скопируйте `.env.sample` в `.env` и заполните переменные.
2. `pip install -r requirements.txt`
3. `python main.py`

## Деплой на Railway

1. Загрузите проект на GitHub.
2. На Railway выберите **New Project → Deploy from GitHub repo**.
3. В разделе **Variables** добавьте переменные из `.env`.
4. Railway автоматически запустит бота (`Procfile`).

## Команды в Telegram

- `/start` — приветствие
- `/toggle_trade` — включить/выключить автоторговлю
- `/status` — статус автоторговли