import glob
import json
import frontmatter
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

TIMEOUT = 10

geocoder = Nominatim(user_agent="mohammadrefat23-github-pages")

addressPoints = []

for filename in glob.glob("_talks/*.md"):

    post = frontmatter.load(filename)

    if "location" not in post:
        continue

    title = post.get("title", "").strip()
    venue = post.get("venue", "").strip()
    location = post.get("location", "").strip()

    try:
        result = geocoder.geocode(location, timeout=TIMEOUT)

        if result is None:
            print(f"Could not geocode: {location}")
            continue

        popup = f"{title}<br />{venue}; {location}"

        addressPoints.append([
            popup,
            result.latitude,
            result.longitude
        ])

        print(f"✓ {location}")

    except GeocoderTimedOut:
        print(f"Timed out: {location}")

with open("talkmap/org-locations.js", "w") as f:
    f.write("var addressPoints = ")
    json.dump(addressPoints, f, indent=2)
    f.write(";")

print(f"\nGenerated {len(addressPoints)} talk locations.")