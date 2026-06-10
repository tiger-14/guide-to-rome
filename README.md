# Guide to Rome

A very basic informational web app for helping the people of ancient Rome to understand its geography and cuisine, and test their knowledge of its history through a trivia quiz.

## Try it

- Run locally — see Quick Start below.

## Quick Start

```bash
pip install flask
python hackathon.py
```

Then open `http://localhost:5000` in your browser.

## Features

- **Home** — landing page introducing the ancient city
- **Maps** — annotated historical map of Rome (27 BCE) with navigation tips
- **Cuisine** — overview of Roman food culture and what citizens ate
- **Quiz** — 5-question interactive trivia with instant right/wrong feedback and a final score

## How it works

The entire app runs as a single Flask file with four routes — `/`, `/maps`, `/food`, and `/quiz`. Each route returns a self-contained HTML page with inline CSS styling. The quiz is made with JavaScript: questions are stored as an array of objects, and the app steps through them, compares the selected answer, shows feedback, then loads the next question after a short delay before displaying a final percentage score.

## Prompt

Built in response to HackForsyth's 2026 hackathon prompt: create a solution to a historical situation.

## Built with

- Python 3
- Flask
- HTML / CSS / JavaScript


## Credits

Built with two teammates during HackForsyth's Hack Club hackathon, September 2025.
