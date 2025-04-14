import logging

from rich.console import Console
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    handlers=[RichHandler(rich_tracebacks=True, console=Console(width=150))],
)
logger = logging.getLogger("blackjack")
