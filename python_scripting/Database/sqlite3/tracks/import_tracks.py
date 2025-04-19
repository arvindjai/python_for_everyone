import sqlite3
import csv

# Connect to (or create) the SQLite database
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Drop tables if they already exist to reset the database
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
''')

# Create normalized tables
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Load CSV file
filename = 'tracks.csv'

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        name = row.get('Name')
        artist = row.get('Artist')
        album = row.get('Album')
        genre = row.get('Genre')
        length = row.get('Total Time')
        rating = row.get('Rating')
        count = row.get('Play Count')

        if name is None or artist is None or album is None or genre is None:
            continue  # Skip incomplete rows

        # Insert Artist
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        # Insert Genre
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        # Insert Album
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        # Insert Track
        cur.execute('''
            INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (name, album_id, genre_id, length, rating, count))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created and data inserted successfully.")