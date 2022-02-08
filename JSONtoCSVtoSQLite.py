import xword_data
import csv, sqlite3


def func(data):
    full_puzzle = [[]]
    full_entry = [[]]
    full_clue = [[]]
    for dict in data:
        for line in dict:
            if line['model'] == "xword_data.puzzle":
                full.append([line['pk'], line['fields']['date'], line['fields']['publisher'], line['fields']['byline'], line['fields']['title']])
            if line['model'] == "xword_data.entry":
                full.append([line['pk'], line['fields']['entry_text']])
            if line['model'] == "xword_data.clue":
                full.append([line['pk'], line['fields']['entry'], line['fields']['clue_text'], line['fields']['theme'], line['fields']['puzzle']])

    return full_puzzle, full_entry, full_clue

data_puzzle, data_entry, data_clue = func(xword_data)
filename = "xword_data_puzzle.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data_puzzle)
filename = "xword_data_entry.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data_entry)
filename = "xword_data_clue.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data_clue)

con = sqlite3.connect(":memory:")
cur = con.cursor()
with open('xword_data_puzzle.csv','r') as fin:
    dr = csv.reader(fin)
    to_db = [(i['col1'], i['col2'], i['col3'], i['col4'], i['col5']) for i in dr]
cur.executemany("INSERT INTO xword_data_puzzle (col5, col2, col4, col3) VALUES (?, ?, ?, ?);", to_db)
with open('xword_data_entry.csv','r') as fin:
    dr = csv.reader(fin)
    to_db = [(i['col1'], i['col2']) for i in dr]
cur.executemany("INSERT INTO xword_data_entry (col2) VALUES (?);", to_db)
with open('xword_data_clue.csv','r') as fin:
    dr = csv.reader(fin)
    to_db = [(i['col1'], i['col2'], i['col3'], i['col4'], i['col5']) for i in dr]
cur.executemany("INSERT INTO xword_data_clue (col2, col5, col3, col4) VALUES (?, ?, ?, ?);", to_db)
con.commit()
con.close()
