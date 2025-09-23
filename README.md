# StreamTracker

## Overview

StreamTracker is an evolution of my original Movie Catalog project. It provides a clean FastAPI backend and UI for managing and tracking movies and TV shows you plan to watch or have already watched. The refactored code organizes the backend into a Python package, making it easy to integrate into larger applications.

## Features

- **Scalable package structure:** All backend code is organized with clear separation of models, schemas, CRUD functions, and the FastAPI entry point.
- **CRUD API:** Endpoints to list, create, read, update, and delete movies and TV shows.
- **SQLite persistence:** A lightweight database stores entertainment data locally.
- **Search and sort:** Search by title or creator and sort results by rating or year.
- **CORS enabled:** The API is configured to accept requests from your local UI or other clients.
- **Modern UI:** A standalone HTML file (see `movie_tracker_ui.html`) lets you interact with the API. It supports light and dark modes and a sleek, responsive design.
- **Poster caching:** Automatically fetches and caches movie/TV show posters to avoid API rate limits.

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

The `movie_tracker_ui.html` file provides a modern front‑end for StreamTracker:

- **Add movies & TV shows:** Enter details like title, director/creator, year, rating, and watched status.
- **List & search:** View all entries, search by keyword, and sort by rating or year.
- **Edit & delete:** Modify existing entries or remove them entirely.
- **Night mode:** Toggle between light and dark themes.
- **Poster caching:** Automatically fetches and caches movie/TV show posters for instant loading.
- **Tabbed interface:** Switch between Movies and TV Shows with dedicated sections.

# Preview:
<img width="2116" height="1946" alt="image" src="https://github.com/user-attachments/assets/fb2b28ed-7cf7-4ab1-b2c4-2bbf056d4f17" />


# Future features:
- [x] **Add notes/review section**
- [x] **TV Shows compatibility**
- [x] **Poster caching system**
- [ ] **Migrate to server/client setup**
- [ ] **Account creation/login**
- [ ] **Add friends to check each other's lists**
- [ ] **Security implementation**
- [ ] **Enhanced search and filtering**
- [ ] **Export/import functionality**

