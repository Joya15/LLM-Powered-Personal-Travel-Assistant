# LLM-Powered Personal Travel Assistant

This project is a personal travel planning assistant built with a large language model (LLM). It collects a user's destination, trip length, interests, budget, climate preference, and travel companions, then generates personalized travel itineraries using prompt engineering and controlled generation settings.

The project was developed for a Macquarie University assignment and has been cleaned into a GitHub portfolio repository with a runnable Python app, sanitized notebook, setup instructions, and assignment report notes.

## Highlights

- LLM-powered itinerary generation using Cohere `command-r-plus`.
- Dialogue-style user profile collection with Python `input()` prompts.
- Prompt engineering for destination, budget, climate, interests, and travel style.
- Temperature testing to compare focused, balanced, and creative generations.
- Sanitized configuration using environment variables instead of hard-coded API keys.
- Portfolio-ready structure with notebook, source code, report notes, and reproducible setup.

## Project Summary

| Area | Description |
| --- | --- |
| Domain | Travel planning and personalized text generation |
| Model | Cohere `command-r-plus` |
| Interface | Command-line dialogue and Jupyter Notebook |
| Core techniques | Prompt engineering, dialogue management, controlled generation |
| Output | Personalized itinerary and travel recommendations |

## Repository Layout

```text
.
|-- travel_assistant_cli.py          # Runnable command-line app
|-- src/travel_assistant/            # Reusable assistant logic
|-- notebooks/                       # Sanitized assignment notebook
|-- docs/                            # Assignment report and project notes
|-- requirements.txt                 # Python dependencies
|-- .env.example                     # Example API-key configuration
|-- .gitignore                       # Local secrets/cache exclusions
`-- LICENSE                          # MIT license
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a local `.env` file:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your Cohere API key:

```text
COHERE_API_KEY=your_cohere_api_key_here
```

Do not commit `.env` to GitHub.

## Run The Assistant

```bash
python travel_assistant_cli.py
```

The app will ask for:

- name
- destination
- trip length
- interests
- budget
- climate preference
- solo or group travel
- preferred creativity level

It then generates a personalized itinerary.

## Example Prompts

```text
Plan a 5-day budget-friendly trip to Sydney for a student interested in nature and street food.
```

```text
Suggest a 3-day beach trip from Sydney under $1000 AUD.
```

```text
Give me a solo travel plan across Southeast Asia for 2 weeks.
```

## Temperature Experiment

The notebook tests the same travel profile with multiple temperature values:

| Temperature | Effect |
| --- | --- |
| 0.3 | More focused and concise |
| 0.7 | Balanced and practical |
| 0.9 | More creative and detailed |

## Notebook

The original assignment notebook has been sanitized before upload:

- removed hard-coded API key
- reads `COHERE_API_KEY` from environment variables
- cleared execution outputs
- preserved assignment workflow and report content

Notebook path:

[notebooks/48571555_Assignment_2_sanitized.ipynb](notebooks/48571555_Assignment_2_sanitized.ipynb)

## My Contribution

I developed the LLM-powered travel assistant workflow, designed prompts for different travel planning scenarios, implemented the dialogue-style input flow, tested multiple generation temperatures, and documented the results in the assignment report. I also packaged the notebook into a clean GitHub project with reusable Python code and safe API-key handling.

## Security Note

API keys should never be stored directly in notebooks or source code. This repository uses `.env` and `COHERE_API_KEY` so credentials stay local.
