import spotipy
import csv
from spotipy.oauth2 import SpotifyOAuth

#####
# This is a work in progress
# Next items:
# - user prompts for output filename
# - dump other things, playlists? saved things? how to format?

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="<SEE SPOTIFY DEV PAGE>",
                                               client_secret="<SEE SPOTIFY DEV PAGE>",
                                               redirect_uri="<READ SPOTIFY DOCS FOR INFO>",
                                               scope="user-follow-read"))

with open('artists_dump.csv', 'w', newline='') as csvfile:
    # we're dumping to a csv file
    csv_writer = csv.writer(csvfile,
                            quotechar=',',# )
                            quoting=csv.QUOTE_MINIMAL)

    # this is our index for pagination
    last_artist_id = None

    while True:
        # grab the first 50, passing none as the "last" 
        results = sp.current_user_followed_artists(limit=50, after=last_artist_id)

        # count down! we will eventually get 0 back.
        results_count = len(results['artists']['items'])
        if results_count == 0:
            break;
        for idx, artist in enumerate(results['artists']['items']):
            artist_name = artist['name']
            artist_id = artist['id']
            # This should be a log statement
            print("Adding: ", artist_name, " ", artist_id)
            csv_writer.writerow([artist_name, artist_id])
            # Get the id of the last artist on the previous page
            last_artist_id = artist_id
