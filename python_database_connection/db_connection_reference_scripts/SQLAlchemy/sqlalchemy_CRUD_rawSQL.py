from sqlalchemy import create_engine

#db_string = "sqlite:///tests.db"

db = create_engine(db_string)

#create
db.execute("DROP TABLE players")
db.execute("CREATE TABLE IF NOT EXISTs players (plyid text, plyname text, runs text)")

#db.execute("TRUNCATE TABLE players")
db.execute("INSERT INTO players(plyid, plyname, runs) VALUES('10001', 'ply1', '100')")
db.execute("INSERT INTO players(plyid, plyname, runs) VALUES('10002', 'ply2', '80')")
db.execute("INSERT INTO players(plyid, plyname, runs) VALUES('10003', 'ply3', '65')")
db.execute("INSERT INTO players(plyid, plyname, runs) VALUES('10004', 'ply4', '95')")
db.execute("INSERT INTO players(plyid, plyname, runs) VALUES('10005', 'ply5', '99')")

# Read

result = db.execute("SELECT * FROM players")

s = [x for x in result]

#Update

db.execute("UPDATE players SET runs = '100' WHERE plyid = '10005'")
q=[x for x in db.execute("SELECT * FROM players")]


#Delete

db.execute("DELETE FROM players  WHERE plyid = '10005'")
e=[x for x in db.execute("SELECT * FROM players")]


print(s)
print(q)
print(e)
s=str(s)
q=str(q)
e=str(e)
with open(".hidden.txt",'w') as f:
	f.write(s)
	
with open(".hidden1.txt",'w') as f:
	f.write(q)

with open(".hidden2.txt",'w') as outfile:
	outfile.write(e)
