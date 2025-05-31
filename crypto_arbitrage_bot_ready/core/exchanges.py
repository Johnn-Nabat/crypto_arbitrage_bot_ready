import ccxt.async_support as ccxt

class ExchangeFactory:
    @staticmethod
    def create(name, creds):
        exchange_class = getattr(ccxt, name)
        return exchange_class({
            "apiKey": creds.get("api_key"),
            "secret": creds.get("api_secret"),
            "password": creds.get("passphrase"),
            "enableRateLimit": True
        })