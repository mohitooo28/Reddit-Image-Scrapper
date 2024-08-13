# Reddit Image Scraper

Reddit Image Scrapper is a Python-based tool designed to automate the process of scraping images from specified subreddits. By simply listing the desired subreddits, users can download images directly to their local machine. This tool is useful for content creators, data collection, or anyone interested in compiling images from Reddit.


## Features

- **Automated Image Scraping:** Scrape images from multiple subreddits at once.
- **Customizable Subreddit List:** Easily add or remove subreddits by editing a text file.
- **Lightweight and Efficient:** Minimal setup and fast scraping.
- **Download Control:** Specify the number of top posts to download images from.

## Pre-requisites:

**1. Python 3.x:** Ensure Python is installed on your system. ([Download Python](https://www.python.org/downloads/))<br>
**2. PIP:** Python package installer should be available.


## Setup:

1. Open command prompt
2. Clone or <a href="https://github.com/mohitooo28/Reddit-Image-Scrapper/archive/refs/heads/main.zip">Download</a> this repository 
    ```
    gh repo clone mohitooo28/Reddit-Image-Scrapper
    ```
3. Install Required Dependencies
    ```
    pip install -r requirements.txt
    ```
4. Create a .env File: In the root directory of the project, create a ```.env``` file and add the following contents:
    ```
    CLIENT_ID      =  your_client_id
    CLIENT_SECRET  =  your_client_secret
    USER_AGENT     =  your_user_agent
    ```
    To obtain your CLIENT_ID, CLIENT_SECRET, and USER_AGENT, refer the following <a href="https://www.reddit.com/dev/api/">Reddit API documentation</a>.
   
4. Add Subreddits:  Open the ```subreddits.txt``` file and add the names of the subreddits you want to scrape images from. Each subreddit should be on a new line.
   

## Usage:

1. Run the program:
    ```
    python reddit_image_scrapper.py
    ```
2. Specify the Number of Posts: When prompted, enter the number of top posts from each subreddit you want to scrape..
3. The images will be saved in the images/ directory within the project folder, organized by subreddit name.

