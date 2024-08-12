import praw
import os
import requests
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'),
                     client_secret=os.getenv('CLIENT_SECRET'),
                     user_agent=os.getenv('USER_AGENT'))


def download_images(subreddit_name, num_posts=10, save_dir='images'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    subreddit = reddit.subreddit(subreddit_name)
    
    print(f"Scraping images from r/{subreddit_name}...")
    
    for submission in subreddit.top(limit=num_posts):
        if submission.url.endswith(('.jpg', '.jpeg', '.png')):
            image_url = submission.url
            
            image_name = image_url.split("/")[-1]
            
            image_path = os.path.join(save_dir, image_name)
            
            with requests.get(image_url) as response:
                with open(image_path, 'wb') as file:
                    file.write(response.content)
            
            print(f"Downloaded: {image_name}")
    
    print(f"Finished downloading images from r/{subreddit_name}\n")

if __name__ == "__main__":
    num_posts = int(input("Enter the number of posts to download images from each subreddit: "))

    with open('subreddits.txt', 'r') as file:
        subreddits = [line.strip() for line in file.readlines()]

    for subreddit in subreddits:
        download_images(subreddit, num_posts=num_posts)