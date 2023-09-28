import os

from db import create_table, create_connection
from query import select_all_from_table
from schema import *

def insert_to_users(conn):
  sql = """
    INSERT INTO users VALUES
    ('beet_farmer', 'Dwight Schrute', 'dwight@schrutebucks.com', 'battlestargalactica'),
    ('worlds_best_boss', 'Michael Scott', 'michaelscott@dundermifflin.com', 'thatswhatshesaid'),
    ('the_paper_guy', 'Jim Halpert', 'jimh@dundermifflin.com', 'pleasehelp'),
    ('nard_dog', 'Andy Bernard', 'andyb@cornell.edu', 'cornell'),
    ('wuphf', 'Ryan Howard', 'ryan@wuphf.com', 'istartedthefire');
  """

  cur = conn.cursor()
  cur.execute(sql)
  conn.commit()
  return cur.lastrowid

def insert_to_videos(conn):
  sql = """
    INSERT INTO videos
    (video_id, name, user_id, date)
    VALUES
    (1, 'Starting the fire', 'wuphf', '2005-10-11'),
    (2, 'How to be the best boss', 'worlds_best_boss', '2008-04-10'),
    (3, 'Getting into Cornell', 'nard_dog', '2004-02-21'),
    (4, 'Planting beets', 'beet_farmer', '2004-05-21'),
    (5, 'Raising beets', 'beet_farmer', '2004-05-22'),
    (6, 'Best places to hide weapons', 'beet_farmer', '2004-05-23'),
    (7, 'Harvesting beets', 'beet_farmer', '2004-05-24'),
    (8, 'Pranks Wars: Jim v Dwight', 'the_paper_guy', '2010-12-12'),
    (9, 'Making W.U.P.H.F.', 'wuphf', '2010-12-12'),
    (10, 'Threat Level Midnight', 'worlds_best_boss', '2011-02-17');
  """

  cur = conn.cursor()
  cur.execute(sql)
  conn.commit()
  return cur.lastrowid


def select_all_from_users(conn):
  cur = conn.cursor()
  cur.execute("SELECT * FROM users")

  rows = cur.fetchall()

  for row in rows:
    print(row)

def main():
  database = "./pythonsqlite.db"
  # Delete the database if its already exists
  if os.path.exists(database):
    os.remove(database)

  # create a database connection
  conn = create_connection(database)
  create_table(conn, sql_create_users_table)
  insert_to_users(conn)
  create_table(conn, sql_create_videos_table)
  insert_to_videos(conn)
  create_table(conn, sql_create_subscriptions_table)
  # insert_to_subscriptions(conn)
  create_table(conn, sql_create_views_table)
  # insert_to_views(conn)
  create_table(conn, sql_create_likes_table)
  # insert_to_likes(conn)
  create_table(conn, sql_create_comments_table)
  # insert_to_comments(conn)

  print("Database build successful!")
  select_all_from_table(conn, 'users')
  select_all_from_table(conn, 'videos')

if __name__ == "__main__":
  main()


