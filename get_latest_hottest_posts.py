import praw

reddit = praw.Reddit(client_id='-qZIPOdSimD2BklZp5PSWw', client_secret='AYKyne5C3GRMAoxUXpDTadvuVxUEwQ', user_agent='WebScraping')


# get 10 hot posts from the MachineLearning subreddit
hot_posts = reddit.subreddit('MachineLearning').hot(limit=10)
for post in hot_posts:
    print(post.title)