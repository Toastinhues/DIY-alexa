
import re
import yt_dlp


def clean(text):
    text = (text or "").lower()
    text = re.sub(r"\([^)]*\)|\[[^]]*\]", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def score_result(title, artist, candidate_title):
    wanted_title = clean(title)
    wanted_artist = clean(artist)
    candidate = clean(candidate_title)

    title_words = set(wanted_title.split())
    artist_words = set(wanted_artist.split())
    candidate_words = set(candidate.split())

    score = 0

    if wanted_title and wanted_title in candidate:
        score += 10
    else:
        score += 8 * len(title_words & candidate_words) / max(len(title_words), 1)

    if wanted_artist and wanted_artist in candidate:
        score += 12
    else:
        score += 10 * len(artist_words & candidate_words) / max(len(artist_words), 1)

    return score


def find_song(title, artist, source=""):
    source = (source or "").lower()

    hints = {
        "com.spotify.music": "official audio",
        "com.google.android.youtube": "official audio",
        "com.google.android.apps.youtube.music": "official audio",
        "com.android.chrome": "",
    }

    query = f"{artist} {title} {hints.get(source, '')}".strip()

    options = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "noplaylist": True,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            data = ydl.extract_info(f"ytsearch5:{query}", download=False)

        candidates = []

        for item in data.get("entries", []) or []:
            if not item:
                continue

            video_title = item.get("title", "")
            video_id = item.get("id", "")

            if not video_title or not re.fullmatch(r"[\w-]{11}", video_id):
                continue

            url = f"https://www.youtube.com/watch?v={video_id}"
            score = score_result(title, artist, video_title)
            candidates.append((score, video_title, url))

        if not candidates:
            return None

        candidates.sort(key=lambda item: item[0], reverse=True)
        score, video_title, url = candidates[0]

        if score < 8:
            return None

        return {
            "title": video_title,
            "url": url,
            "score": round(score, 2),
        }

    except Exception as error:
        print(f"Search failed: {error}")
        return None
