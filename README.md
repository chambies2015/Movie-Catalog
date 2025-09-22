# Movie Tracker

## Overview

Movie Tracker is an evolution of my original Movie Catalog project. It provides a clean FastAPI backend and UI for managing and tracking movies you plan to watch or have already watched. The refactored code organizes the backend into a Python package called `movie_tracker`, making it easy to integrate into larger applications.

## Features

- **Scalable package structure:** All backend code is organized under `movie_tracker`, with clear separation of models, schemas, CRUD functions, and the FastAPI entry point.
- **CRUD API:** Endpoints to list, create, read, update, and delete movies.
- **SQLite persistence:** A lightweight database stores movie data locally.
- **Search and sort:** Search by title or director and sort results by rating or year.
- **CORS enabled:** The API is configured to accept requests from your local UI or other clients.
- **Modern UI:** A standalone HTML file (see `movie_tracker_ui.html`) lets you interact with the API. It supports light and dark modes and a sleek, responsive design.

## Running the API

1. Create a virtual environment and install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

2. Start the server:
   Run the start.bat to start the server and automatically open the UI file.

   If you want the movie posters for each entry, you'll need to obtain a OMDB api key and plug it into sampleCredentials.js then rename the file to just credentials.js

   The API will be available at `http://127.0.0.1:8000`. Visit `http://127.0.0.1:8000/docs` for interactive Swagger documentation.

   The UI will automatically open in default browswer 5 seconds after uvicorn server startup.

## Using the UI

The `movie_tracker_ui.html` file provides a modern front‑end for your tracker:

- **Add movies:** Enter a title, director, year, rating, and watched flag.
- **List & search:** View all movies, search by keyword, and sort by rating or year.
- **Edit & delete:** Modify existing entries or remove them entirely.
- **Night mode:** Toggle between light and dark themes.
- **Movie posters:** Each movie entry will search for related move poster and show it for each entry.

# Preview:
<img width="2085" height="1945" alt="image" src="https://github.com/user-attachments/assets/bcf75d99-617e-4782-8e7f-c57fb9ea9be6" />

# Future features:
- **Migrate to server/client setup**
- **Account creation/login**
- **Add friends to check each others lists**
- **Security implementation**
- **TV Shows compatibility**

