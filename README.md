# Guide to Rome

An interactive web app for exploring ancient Rome — its geography, cuisine, and history — complete with a trivia quiz.

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

The entire app runs as a single Flask file with four routes — `/`, `/maps`, `/food`, and `/quiz`. Each route returns a self-contained HTML page with inline CSS styling. The quiz is client-side JavaScript: questions are stored as an array of objects, and the app steps through them, compares the selected answer, shows feedback, then loads the next question after a short delay before displaying a final percentage score.

The choice to keep everything in one Python file was deliberate for the hackathon context — faster iteration, nothing to import or configure, easy to hand off to teammates mid-session.

## Built with

- Python 3
- Flask
- HTML / CSS / vanilla JavaScript
- Google Fonts (Great Vibes, Tinos)

## Credits

Built with two teammates during a HackForsyth's Hack Club hackathon, September 2025.
