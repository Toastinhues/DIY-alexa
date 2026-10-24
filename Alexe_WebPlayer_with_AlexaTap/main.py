
import os
import time
import subprocess
import requests
import yt_dlp

from track_search import find_song

API_URL = os.getenv(
    "DIY_ALEXA_API_URL",
    "https://diy-alexa-website.onrender.com/api/last-track"
)

VLC_PATH = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
POLL_SECONDS = 5

last_seen_track = None
player_process = None


def fetch_latest_track():
    try:
        response = requests.get(API_URL, timeout=60)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict):
            return None

        title = data.get("title")
        artist = data.get("artist")

        if not isinstance(title, str) or not isinstance(artist, str):
            return None

        title = title.strip()
        artist = artist.strip()

        if not title or not artist:
            return None

        return {
            "title": title[:250],
            "artist": artist[:250],
            "source": str(data.get("source", ""))[:150],
            "received_at": str(data.get("received_at", ""))[:100],
        }

    except (requests.RequestException, ValueError) as error:
        print("Website error:", error)
        return None


def resolve_audio_url(video_url):
    """Resolve a YouTube page into a direct audio-stream URL."""
    options = {
        "format": "bestaudio/best",
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "skip_download": True,
    }

    try:
        print("Resolving audio stream with yt-dlp...")

        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(video_url, download=False)

        if info and info.get("url"):
            return info["url"]

        print("yt-dlp did not return an audio URL.")

    except Exception as error:
        print("Audio extraction failed:", error)

    return None


def stop_current_player():
    global player_process

    if player_process and player_process.poll() is None:
        print("Stopping previous playback...")
        player_process.terminate()

        try:
            player_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            player_process.kill()
            player_process.wait()

    player_process = None


def play_result(result):
    global player_process

    if not result:
        print("No close match found.")
        return

    if not os.path.isfile(VLC_PATH):
        print("VLC not found:", VLC_PATH)
        return

    print("Selected:", result["title"])
    print("Match score:", result["score"])
    print("Video:", result["url"])

    audio_url = resolve_audio_url(result["url"])

    if not audio_url:
        print("Could not get a playable audio stream.")
        return

    stop_current_player()

    print("Starting audio in VLC...")

    try:
        player_process = subprocess.Popen([
            VLC_PATH,
            "--no-video",
            "--play-and-exit",
            audio_url,
        ])

        time.sleep(3)

        if player_process.poll() is not None:
            print("VLC exited with code:", player_process.returncode)
            print("VLC could not continue playing this stream.")
        else:
            print("VLC is running. Check your speakers and volume.")

    except OSError as error:
        print("Could not launch VLC:", error)


def main():
    global last_seen_track

    print("===================================")
    print("       DIY ALEXA PLAYER")
    print("===================================")
    print("Website:", API_URL)
    print("Audio player: VLC + yt-dlp")
    print("Press Ctrl+C to stop.")
    print()

    while True:
        track = fetch_latest_track()

        if track:
            track_id = (
                track["title"].casefold(),
                track["artist"].casefold(),
                track["received_at"],
            )

            if track_id != last_seen_track:
                last_seen_track = track_id

                print("\nNew track detected!")
                print("Song:", track["title"])
                print("Artist:", track["artist"])
                print("Source app:", track["source"] or "Unknown")

                result = find_song(
                    track["title"],
                    track["artist"],
                    track["source"],
                )

                play_result(result)

        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopping DIY Alexa player...")
        stop_current_player()
        print("Player stopped.")
