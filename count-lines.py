import urllib

def process_file(filename):
    songs = dict()
    # file = open("./recommended-guitar-songs")
    file = open(filename)

    for line in file:
        if line in songs:
            songs[line] += 1
        else:
            songs[line] = 1

    out = open("most-" + filename, "w")

    for song, recommendation_count in sorted(songs.items(), key=lambda x: x[1], reverse=True):
        line = "* {}: [{}](https://www.songsterr.com/a/wa/search?pattern={})\n".format(str(recommendation_count), song.replace('\n', ''), urllib.quote(song.replace("-", "")))
        out.write(line)

process_file("recommended-guitar-songs-beginner")
process_file("recommended-guitar-songs-intermediate")
process_file("recommended-guitar-songs-advanced")
