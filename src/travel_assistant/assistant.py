"""Core logic for the LLM-powered personal travel assistant."""

from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterable

import cohere
from dotenv import load_dotenv


DEFAULT_MODEL = "command-r-plus"


@dataclass
class TravelProfile:
    """User preferences collected through the dialogue flow."""

    name: str
    destination: str
    days: str
    interests: str
    budget: str = ""
    climate: str = ""
    companions: str = ""

    def to_prompt_context(self) -> str:
        parts = [
            f"Traveler name: {self.name}",
            f"Destination: {self.destination}",
            f"Trip length: {self.days} days",
            f"Interests: {self.interests}",
        ]

        if self.budget:
            parts.append(f"Budget: {self.budget}")
        if self.climate:
            parts.append(f"Preferred climate: {self.climate}")
        if self.companions:
            parts.append(f"Travel companions: {self.companions}")

        return "\n".join(parts)


class CohereTravelAssistant:
    """Wrapper around Cohere generation for travel itinerary prompts."""

    def __init__(
        self,
        api_key: str | None = None,
        model: str = DEFAULT_MODEL,
        max_tokens: int = 1200,
        temperature: float = 0.7,
    ) -> None:
        load_dotenv()
        self.api_key = api_key or os.getenv("COHERE_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "COHERE_API_KEY is not set. Create a .env file or export the key before running."
            )

        self.client = cohere.Client(self.api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def generate(self, prompt: str, temperature: float | None = None, max_tokens: int | None = None) -> str:
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            max_tokens=max_tokens or self.max_tokens,
            temperature=self.temperature if temperature is None else temperature,
        )
        return response.generations[0].text.strip()

    def build_itinerary_prompt(self, profile: TravelProfile) -> str:
        return f"""
You are a helpful personal travel assistant.

Create a practical, personalized travel itinerary using the traveler's profile below.
Make the plan easy to follow, budget-aware, and aligned with the user's interests.

Traveler profile:
{profile.to_prompt_context()}

Return:
1. Short overview
2. Day-by-day itinerary
3. Suggested food or local experiences
4. Budget and transport tips
5. Final recommendation
""".strip()

    def generate_itinerary(self, profile: TravelProfile, temperature: float | None = None) -> str:
        return self.generate(self.build_itinerary_prompt(profile), temperature=temperature)

    def compare_temperatures(self, prompt: str, temperatures: Iterable[float] = (0.3, 0.7, 0.9)) -> dict[float, str]:
        return {
            temp: self.generate(prompt, temperature=temp, max_tokens=400)
            for temp in temperatures
        }

