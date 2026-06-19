"""Command-line interface for the LLM-powered personal travel assistant."""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from travel_assistant import CohereTravelAssistant, TravelProfile


def ask(prompt: str) -> str:
    return input(prompt).strip()


def choose_temperature() -> float:
    value = ask("Creativity level: focused, balanced, or creative? [balanced] ")
    options = {
        "focused": 0.3,
        "balanced": 0.7,
        "creative": 0.9,
        "": 0.7,
    }
    return options.get(value.lower(), 0.7)


def main() -> None:
    print("LLM-Powered Personal Travel Assistant")
    print("-------------------------------------")

    profile = TravelProfile(
        name=ask("What's your name? "),
        destination=ask("Where do you want to travel? "),
        days=ask("How many days will you be staying? "),
        interests=ask("What kind of travel do you prefer? "),
        budget=ask("What's your estimated budget? "),
        climate=ask("What kind of climate do you prefer? "),
        companions=ask("Are you traveling solo or with someone? "),
    )

    temperature = choose_temperature()
    assistant = CohereTravelAssistant(temperature=temperature)
    itinerary = assistant.generate_itinerary(profile)

    print("\n--- Personalized Travel Plan ---")
    print(itinerary)


if __name__ == "__main__":
    main()

