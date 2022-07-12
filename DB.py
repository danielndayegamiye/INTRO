import sqlite3
fichierDonnees = "D:/Musique"
conn = sqlite3.connect(fichierDonnees)
cur = conn.cursor()
cur.execute("CREATE TABLE Compositeurs (comp TEXT, a_naiss INTEGER, a_mort INTEGER)")
data = [('Mozart', 1756, 1791),
      ('Beethoven', 1770, 1827),
     ('Haendel', 1685, 1759),
     ('Schubert', 1797, 1828),
     ('Vivaldi', 1678, 1741),
     ('Monteverdi', 1567, 1643),
     ('Chopin', 1810, 1849),
     ('Bach', 1685, 1750),
     ('Shostakovich', 1906, 1975)]
for tu in data:
    cur.execute("INSERT INTO Compositeurs(comp,a_naiss,a_mort) VALUES (?,?,?)", tu)
cur.execute("CREATE TABLE Oeuvres (comp TEXT, titre TEXT, duree INTEGER, interpr TEXT)")
data1 = [('Vivaldi', 'Les quatre saisons', 20, 'T. Pinnock'),
       ('Mozart', 'Concerto piano N°12', 25, 'M. Perahia'),
       ('Brahms', 'Concerto violon N°2', 40, 'A. Grumiaux'),
       ('Beethoven', 'Sonate "au clair de lune"', 14, 'W. Kempf'),
       ('Beethoven', 'Sonate "pathétique"', 17, 'W. Kempf'),
       ('Schubert', 'Quintette "la truite"', 39, 'SE of London'),
       ('Haydn', 'La création', 109, 'H. Von Karajan'),
       ('Chopin', 'Concerto piano N°1', 42, 'M.J. Pires'),
       ('Bach', 'Toccata & fugue', 9, 'P. Burmester'),
       ('Beethoven', 'Concerto piano N°4', 33, 'M. Pollini'),
       ('Mozart', 'Symphonie N°40', 29, 'F. Bruggen'),
       ('Mozart', 'Concerto piano N°22', 35, 'S. Richter'),
       ('Beethoven', 'Concerto piano N°3', 37, 'S. Richter')]
for tu in data1:
    cur.execute("INSERT INTO Oeuvres(comp,titre,duree,interpr) VALUES (?,?,?,?)", tu)
conn.commit()
cur.close()
conn.close()
