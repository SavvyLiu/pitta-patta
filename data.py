# import requests
# import csv

# API_KEY = 'AIzaSyD1jbepwPDnaxB-mjquD_Z8z-hOLKuK8IY'

# CHANNEL_NAME = 'WhatYuhKnow'
# CHANNEL_NAME2 = 'machelmontanomusic'
# CHANNEL_NAME3 = 'JulianspromosTV'
# BASE_URL = 'https://www.googleapis.com/youtube/v3/'

# # Step 1: Get the channel ID for the custom URL
# def get_channel_id(channel_name, api_key):
#     url = f"{BASE_URL}search?part=snippet&type=channel&q={channel_name}&key={api_key}"
#     response = requests.get(url).json()
#     channel_id = response['items'][0]['id']['channelId']
#     return channel_id

# # Step 2: Get videos from the channel
# def get_videos(channel_id, api_key):
#     url = f"{BASE_URL}search?part=id&channelId={channel_id}&maxResults=50&order=date&type=video&key={api_key}"
#     response = requests.get(url).json()
#     return [item['id']['videoId'] for item in response.get('items', [])]

# # Step 3: Get comments for a video
# def get_comments(video_id, api_key):
#     url = f"{BASE_URL}commentThreads?part=snippet&videoId={video_id}&key={api_key}"
#     response = requests.get(url).json()
#     comments = [item['snippet']['topLevelComment']['snippet']['textOriginal'] for item in response.get('items', [])]
#     return comments

# # Fetching comments from the "What Yuh Know" channel
# channel_id = get_channel_id(CHANNEL_NAME, API_KEY)
# videos = get_videos(channel_id, API_KEY)
# all_comments = []

# for video in videos:
#     comments = get_comments(video, API_KEY)
#     all_comments.extend(comments)

# #Machel comments
# channel_id_MM = get_channel_id(CHANNEL_NAME2, API_KEY)
# videosMM = get_videos(channel_id, API_KEY)

# for video in videosMM:
#     comments = get_comments(video, API_KEY)
#     all_comments.extend(comments)

# #Bunji Comments
# channel_id_BG = get_channel_id(CHANNEL_NAME3, API_KEY)
# videosBG = get_videos(channel_id, API_KEY)

# for video in videosBG:
#     comments = get_comments(video, API_KEY)
#     all_comments.extend(comments)


# # print(all_comments)




import requests
import csv

API_KEY = 'AIzaSyD1jbepwPDnaxB-mjquD_Z8z-hOLKuK8IY'

# Channel names (change these as needed)
CHANNEL_NAME1 = 'WhatYuhKnow'
CHANNEL_NAME2 = 'MachelMontano'
CHANNEL_NAME3 = 'BujuBanton'
CHANNEL_NAME4 = 'YohanPartap'
CHANNEL_NAME5 = 'TrinidadSlang'

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

# Fetching comments from Bunji
channel_id_BG = get_channel_id(CHANNEL_NAME3, API_KEY)

if channel_id_BG:
    videos_BG = get_videos(channel_id_BG, API_KEY)
    for video in videos_BG:
        comments = get_comments(video, API_KEY)
        all_comments.extend(comments)


# Fetching comments from Yohan
channel_id_YP = get_channel_id(CHANNEL_NAME4, API_KEY)

if channel_id_YP:
    videos_YP = get_videos(channel_id_BG, API_KEY)
    for video in videos_YP:
        comments = get_comments(video, API_KEY)
        all_comments.extend(comments)

# Fetching comments from Channel 5
channel_id_5 = get_channel_id(CHANNEL_NAME5, API_KEY)

if channel_id_5:
    videos_5 = get_videos(channel_id_5, API_KEY)
    for video in videos_5:
        comments = get_comments(video, API_KEY)
        all_comments.extend(comments)

# Save all comments to CSV
save_comments_to_csv(all_comments, 'youtube_comments.csv')

print(f"Saved {len(all_comments)} comments to 'youtube_comments.csv'")
