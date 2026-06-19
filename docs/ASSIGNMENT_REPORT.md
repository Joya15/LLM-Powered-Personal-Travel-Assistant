# Assignment Report

## Explanation of Code

This assignment created a personal travel assistant application powered by Cohere's `command-r-plus` large language model. The assistant interacts with users, gathers travel-related information, and generates personalized itineraries.

The original implementation was written in Python inside a Jupyter Notebook. It used `input()` prompts to collect the traveler's name, destination, trip length, interests, budget, climate preference, and travel companions. These inputs were combined into a structured prompt and passed to the Cohere LLM using the `.generate()` function.

The GitHub version keeps the same assignment workflow but moves reusable logic into Python source files. It also removes hard-coded credentials and reads the API key from the `COHERE_API_KEY` environment variable.

## Prompting Approach

The assistant uses prompt engineering to guide the LLM toward practical travel planning. The prompt asks for a short overview, day-by-day itinerary, food and local experiences, budget/transport tips, and a final recommendation.

## Explanation of Results

Several travel planning scenarios were tested:

- Food-focused 10-day trip to Thailand.
- 3-day beach trip from Sydney under $1000 AUD.
- Romantic weekend getaway in Italy.
- 2-week solo Southeast Asia trip.
- Vegetarian-friendly cities in Europe.

The model generated personalized travel recommendations that reflected different destinations, budgets, interests, and travel styles.

## Temperature Testing

The same prompt was tested with different temperature values:

- `0.3`: more precise and concise recommendations.
- `0.7`: balanced, informative, and engaging itineraries.
- `0.9`: more creative and richly detailed responses.

This showed how generation settings can change the style and specificity of LLM output.

