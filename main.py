from auto import auto_follow
from auto import auto_fav
from auto import auto_rt

#this is a sample program to use the auto.py script
auto_fav("ubuntu", count=1)
auto_fav("teamfollow", count=1)
auto_fav("teamfollowback", count=0)
auto_follow("funny", count=1)
auto_follow("lol", count=1)
auto_follow("beautiful", count=1)
auto_unfollow_nonfollowers("funny", count=1)
auto_rt("funny", count=1)
auto_follow_followers("follow", count=1) auto_follow("followforfollow", count=1)

#auto follow 10 users who come when we search for keyword "followback"
auto_follow("followback", count=1)
auto_follow("teamfollow", count=1)

