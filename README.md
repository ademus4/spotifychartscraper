# spotifychartscraper
A program to collect the past 100 days of Spotify Charts data for analysis

## Contents

| File                   | Description     |
|------------------------|-----------------|
| models.py              | Database tables and relationships |
| utils.py               | Functions for use with scrapers and initialisation |
| init_db.py             | Initialises database with 100 day objects |
| scrape_top200.py       | Downloads CSV files from the Spotify Charts website for the top 200 streamed tracks |
| scrape_viral50.py      | As above but for the viral 50 chart |
| Top 200 Charts.ipynb   | Main analysis of the data, contains tables and charts |
| schema_diagram.pdf     | A visualisation of the database schema |
| schema_diagram.mwb     | As above |
| db_backup_20170417.sql | A copy of the raw data used in the analysis|
