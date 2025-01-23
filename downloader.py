import yt_dlp

def download_youtube_video(url, output_folder="downloads"):
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Choose the best quality
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Save as title.extension in output_folder
        'merge_output_format': 'mp4',  # Merge video and audio into mp4 format
    }

    # Create the output folder if it doesn't exist
    import os
    os.makedirs(output_folder, exist_ok=True)

    # Use yt-dlp to download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

youtube_url = input("Enter the YouTube video URL: ")
download_youtube_video(youtube_url)