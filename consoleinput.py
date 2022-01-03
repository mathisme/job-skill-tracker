import sqlite3

skills = []
ranks = []
con = sqlite3.connect('data.db')
cur = con.cursor()
title = input("Enter job title:  ")
skill = ''
while skill.lower() != 'done':
    skill = input("Enter the skill or 'done' if done:  ")
    if skill.lower()=='done':
        continue
    rank = int(input("Enter your skill rank (1 - 5) where 1 is no skill and 5 is very skilled:  "))
    cur.execute("insert into skills values (?, ?, ?)", (title, skill, rank))
con.commit()
con.close()
    