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
- **Export/Import functionality:** Export all your data to JSON format or import data from JSON files with conflict resolution.
- **Statistics Dashboard:** Comprehensive analytics showing watch progress, rating distributions, year analysis, and director statistics with beautiful visualizations.

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

## Export/Import Functionality

StreamTracker now includes powerful export/import capabilities:

### Exporting Data
- Click the **"Export Data"** button in either the Movies or TV Shows tab
- Your entire collection will be downloaded as a JSON file with timestamp
- The export includes all metadata: titles, directors, years, ratings, reviews, watched status, and poster URLs
- Export files are named `streamtracker-export-YYYY-MM-DD.json`

### Importing Data
- Click the **"Import Data"** button in either tab to select a JSON file
- The system will automatically detect and import movies and TV shows
- **Smart conflict resolution**: Existing entries (matched by title + director for movies, title + year for TV shows) will be updated rather than duplicated
- Import results show how many items were created vs updated
- Any errors during import are reported for easy troubleshooting

### API Endpoints
The export/import functionality is also available via API:
- `GET /export/` - Export all data as JSON
- `POST /import/` - Import data from JSON payload
- `POST /import/file/` - Import data from uploaded JSON file

## Statistics Dashboard

StreamTracker includes a comprehensive statistics dashboard accessible via the **📊 Statistics** tab:

### Watch Progress Analytics
- **Total items** in your collection (movies + TV shows)
- **Watched vs. unwatched** counts and percentages
- **Visual progress bar** showing completion status
- **Separate tracking** for movies and TV shows

### Rating Analysis
- **Average rating** across all rated items
- **Rating distribution** with interactive bar charts (1-10 scale)
- **Highest rated items** showing your top-rated movies and TV shows
- **Visual representation** of your rating patterns

### Year Analysis
- **Oldest and newest** years in your collection
- **Decade breakdown** with bar charts showing distribution across decades
- **Year-based insights** to understand your viewing preferences over time

### Director Statistics
- **Most prolific directors** (directors with the most movies in your collection)
- **Highest rated directors** (directors with the best average ratings)
- **Director insights** to discover your favorite filmmakers

### API Endpoints
The statistics are also available via API:
- `GET /statistics/` - Complete statistics dashboard
- `GET /statistics/watch/` - Watch progress statistics
- `GET /statistics/ratings/` - Rating analysis
- `GET /statistics/years/` - Year-based statistics
- `GET /statistics/directors/` - Director statistics

## Using the UI

The `movie_tracker_ui.html` file provides a modern front‑end for StreamTracker:

- **Add movies & TV shows:** Enter details like title, director/creator, year, rating, and watched status.
- **List & search:** View all entries, search by keyword, and sort by rating or year.
- **Edit & delete:** Modify existing entries or remove them entirely.
- **Night mode:** Toggle between light and dark themes.
- **Poster caching:** Automatically fetches and caches movie/TV show posters for instant loading.
- **Tabbed interface:** Switch between Movies, TV Shows, and Statistics with dedicated sections.
- **Export/Import:** Export your entire collection to JSON or import data from JSON files with smart conflict resolution.
- **Statistics Dashboard:** Comprehensive analytics with watch progress, rating distributions, year analysis, and director insights.

# Preview:
<img width="2116" height="1946" alt="image" src="https://github.com/user-attachments/assets/fb2b28ed-7cf7-4ab1-b2c4-2bbf056d4f17" />


# Future features:
- [x] **Add notes/review section**
- [x] **TV Shows compatibility**
- [x] **Poster caching system**
- [x] **Export/import functionality**
- [x] **Statistics dashboard**
- [ ] **Migrate to server/client setup**
- [ ] **Account creation/login**
- [ ] **Add friends to check each other's lists**
- [ ] **Security implementation**
- [ ] **Enhanced search and filtering**

