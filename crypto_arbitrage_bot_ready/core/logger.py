import logging, os, pathlib
log_dir = pathlib.Path("logs")
log_dir.mkdir(exist_ok=True)

logger = logging.getLogger("arb_bot")
logger.setLevel(logging.INFO)
fh = logging.FileHandler(log_dir / "bot.log")
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(fh)