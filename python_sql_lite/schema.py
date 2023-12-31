sql_create_users_table = """
  CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT
  );
"""

sql_create_videos_table = """
  CREATE TABLE videos (
    video_id INT AUTO_INCREMENT PRIMARY KEY,
    name TEXT,
    user_id TEXT,
    date DATE,
    FOREIGN KEY (user_id) references users(user_id)
  );
"""

sql_create_subscriptions_table = """
  CREATE TABLE subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY,
    creator_id TEXT,
    subscriber_id TEXT,
    FOREIGN KEY (creator_id) references users(user_id),
    FOREIGN KEY (subscriber_id) references users(user_id)
  );
"""

sql_create_views_table = """
  CREATE TABLE views (
    view_id INT AUTO_INCREMENT PRIMARY KEY,
    video_id INT,
    user_id TEXT,
    FOREIGN KEY (video_id) references videos(video_id),
    FOREIGN KEY (user_id) references users(user_id)
  );
"""

sql_create_likes_table = """
  CREATE TABLE likes (
    like_id INT AUTO_INCREMENT PRIMARY KEY,
    video_id INT,
    user_id TEXT,
    FOREIGN KEY (video_id) references videos(video_id),
    FOREIGN KEY (user_id) references users(user_id)
  );
"""

sql_create_comments_table = """
  CREATE TABLE comments (
    comment_id INT AUTO_INCREMENT PRIMARY KEY,
    video_id INT,
    user_id TEXT,
    date DATETIME,
    content TEXT,
    FOREIGN KEY (video_id) references videos(video_id),
    FOREIGN KEY (user_id) references users(user_id)
  );
"""

def get_schema():
  schema = f"{sql_create_users_table}" \
           f"{sql_create_videos_table}" \
           f"{sql_create_subscriptions_table}" \
           f"{sql_create_views_table}" \
           f"{sql_create_likes_table}" \
           f"{sql_create_comments_table}"
  return schema
