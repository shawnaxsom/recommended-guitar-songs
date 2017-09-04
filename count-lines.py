import urllib

songs = dict()
file = open("./recommended-guitar-songs")

for line in file:
    if line in songs:
        songs[line] += 1
    else:
        songs[line] = 1

out = open("./most-recommended-guitar-songs", "w")

for song, recommendation_count in sorted(songs.items(), key=lambda x: x[1], reverse=True):
    line = "{}: ({})[https://www.songsterr.com/a/wa/search?pattern={}]\n".format(str(recommendation_count), song.replace('\n', ''), urllib.quote(song))
    out.write(line)

