from auto import auto_follow
from auto import auto_fav
from auto import auto_follow_followers
from twitter_follow_bot import auto_rt
import time

#this is a sample program to use the auto.py script

auto_rt("funny", count=10)
auto_follow_followers("follow", count=100) auto_follow("followforfollow", count=10)
auto_follow("funny", count=10)
auto_follow("lol", count=10)
auto_follow("beautiful", count=10)

#auto follow 10 users who come when we search for keyword "followback"

auto_fav("lol", count=20)
auto_fav("funny", count=20)
auto_fav("amusing", count=20)
auto_fav("beautiful", count=20)
