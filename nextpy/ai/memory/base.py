# This file has been modified by the Nextpy Team in 2023 using AI tools and automation scripts. 
# We have rigorously tested these modifications to ensure reliability and performance. Based on successful test results, we are confident in the quality and stability of these changes.

from abc import ABC, abstractmethod
from typing import Any, Dict, List

from pydantic import BaseModel, Field

from nextpy.ai.schema import BaseMessage


class BaseMemory(ABC, BaseModel):
    """Abstract base class for memory management in a chatbot application.
    This class defines the interface for setting, getting, and checking existence of data in memory.
    """

    llm: Any = None
    memory_threshold: int = 1
    # All memories are stored in this list
    messages: List[Dict[BaseMessage, Any]] = Field(default=list())

    @abstractmethod
    def add_memory(self, prompt: str, llm_response: Any) -> None:
        """Add a memory to the store."""
        pass

    @abstractmethod
    def get_memory(self, **kwargs) -> str:
        """Retrieve entire memory from the store."""
        pass

    @abstractmethod
    def remove_memory(self, prompt: str) -> None:
        """Remove a memory from the store."""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clear all memories."""
        pass

    @property
    def memory_prompts(self) -> List[str]:
        """Return the prompts for all memories."""
        prompts = []
        for conversation in self.messages:
            prompts.append(conversation["prompt"])

        return prompts
