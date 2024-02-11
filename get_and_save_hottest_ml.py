import praw
import pandas as pd
posts = []

reddit = praw.Reddit(client_id='-qZIPOdSimD2BklZp5PSWw', client_secret='AYKyne5C3GRMAoxUXpDTadvuVxUEwQ', user_agent='WebScraping')
ml_subreddit = reddit.subreddit('MachineLearning')
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)
