# botato/client.py
# -*- coding: utf-8 -*-

from typing import Callable, Awaitable, Dict, List, TypeVar
from loguru import logger

from botato.gateway.connection import GatewayConnection
from botato.http.client import HTTPClient

T = TypeVar('T', bound=Callable[..., Awaitable[None]])


class BotatoClient:
    """
    Main client class for interacting with the Discord API.
    
    This class handles Gateway connectivity, HTTP communication,
    and user-defined event registration and dispatching.
    """
    
    def __init__(self, token: str) -> None:
        """
        Initialize the BotatoClient with the provided token.

        Args:
            token (str): Discord bot token used for authentication.
        """
        self.token: str = token.strip()
        self.gateway: GatewayConnection | None = None
        self.http: HTTPClient | None = None
        self._event_handlers: Dict[str, List[T]] = {}
        
        logger.debug("BotatoClient initialized.")
        
    async def connect(self) -> None:
        """
        Connect to the Discord Gateway and start listening for events.
        """
        logger.info("Starting BotatoClient connection...")
        
        self.http = HTTPClient(self.token)
        self.gateway = GatewayConnection(self.token, self._handle_event)
        await self.gateway.connect()
        
    def event(self, func: T) -> T:
        """
        Decorator to register an event handler.
        
        The function name should match the event name from Discord,
        e.g., 'on_message_create', 'on_ready';

        Args:
            func (Callable): The function to be registered as an event handler.
        Returns:
            Callable: The original function, now registered as an event handler.
        """
        event_name = func.__name__
        if not event_name.startswith("on_"):
            raise ValueError("Event handler function name must start with 'on_'")
        
        logger.debug(f"Registering event handler: {event_name}")
        self._event_handlers.setdefault(event_name, []).append(func)
        return func
    
    async def _handle_event(self, event_name: str, data: dict) -> None:
        """
        Internal method to dispatch an event to registered handlers;

        Args:
            event_name (str): Discord event name (e.g., 'MESSAGE_CREATE').
            data (dict): Raw event payload
        """
        handler_key = f"on_{event_name.lower()}"
        if handlers := self._event_handlers.get(handler_key):
            for handler in handlers:
                try:
                    await handler(data)
                except Exception as e:
                    logger.exception(f"Error in event handler '{handler_key}': {e}")
        else:
            logger.debug(f"No handler registered for event: {handler_key}")
        
    async def close(self) -> None:
        """
        Close the connection to Discord and clean up resources.
        """
        logger.info("Closing BotatoClient...")
        if self.gateway:
            await self.gateway.close()
        if self.http:
            await self.http.close()