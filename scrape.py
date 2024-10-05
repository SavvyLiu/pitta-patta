import requests
import config
import csv

API_KEY = config.api_key

# Channel names (change these as needed)
CHANNEL_NAME1 = 'WhatYuhKnow'
CHANNEL_NAME2 = 'MachelMontano'
CHANNEL_NAME3 = 'BujuBanton'
BASE_URL = 'https://www.googleapis.com/youtube/v3/'

# Step 1: Get the channel ID for the custom URL (for custom channel names)
def get_channel_id(channel_name, api_key):
    url = f"{BASE_URL}search?part=snippet&type=channel&q={channel_name}&key={api_key}"
    response = requests.get(url).json()
    if 'items' in response and len(response['items']) > 0:
        channel_id = response['items'][0]['id']['channelId']
        return channel_id
    else:
        print(f"No channel found for {channel_name}")
        return None

# Step 2: Get videos from the channel
def get_videos(channel_id, api_key):
    url = f"{BASE_URL}search?part=id&channelId={channel_id}&maxResults=50&order=date&type=video&key={api_key}"
    response = requests.get(url).json()
    return [item['id']['videoId'] for item in response.get('items', [])]

# Step 3: Get comments for a video
def get_comments(video_id, api_key):
    url = f"{BASE_URL}commentThreads?part=snippet&videoId={video_id}&key={api_key}"
    response = requests.get(url).json()
    comments = [item['snippet']['topLevelComment']['snippet']['textOriginal'] for item in response.get('items', [])]
    return comments

# Step 4: Save comments to a CSV file
def save_comments_to_csv(comments, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Comment'])  # Header row
        for comment in comments:
            writer.writerow([comment])

# Fetching comments from What Yuh Know
all_comments = []
channel_id = get_channel_id(CHANNEL_NAME1, API_KEY)

if channel_id:
    videos = get_videos(channel_id, API_KEY)
    for video in videos:
        comments = get_comments(video, API_KEY)
        all_comments.extend(comments)

# Fetching comments from Machel Montano
channel_id_MM = get_channel_id(CHANNEL_NAME2, API_KEY)

if channel_id_MM:
    videos_MM = get_videos(channel_id_MM, API_KEY)
    for video in videos_MM:
        comments = get_comments(video, API_KEY)
        all_comments.extend(comments)

# Fetching comments from Buju Banton
channel_id_BG = get_channel_id(CHANNEL_NAME3, API_KEY)

if channel_id_BG:
    videos_BG = get_videos(channel_id_BG, API_KEY)
    for video in videos_BG:
        comments = get_comments(video, API_KEY)
        all_comments.extend(comments)

# Save all comments to CSV
save_comments_to_csv(all_comments, 'youtube_comments.csv')
print(f"Saved {len(all_comments)} comments to 'youtube_comments.csv'")
