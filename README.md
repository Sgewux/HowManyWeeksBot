# HowManyWeeksBot
HowManyWeeks it's a Twitter bot developed by Sebastian Andrade Cedano. Its main pourpose is to tweet every week how many weeks are left to finish the current year, Also the bot can reply to you if you tag it in a new tweet, if you tag it in a reply to other tweet the bot wont reply to you.


## How does it work?

How many weeks bot works with the Twitter API, every 60 seconds the bot will scrape the last tweet where someone tagged it, after that the bot will check if this tweet is a new mention or if the tweet is an old mention. Also the bot will check if the tweet was not a reply to other tweet if both conditions have returned true the bot will reply random stuff (you can see the random replies list in the code) and also the bot will mark your mention as favorite. Also every wednesday the bot will tweet how many weeks left to finish the current year.

## Requirements

- Tweepy 3.10.0

- Schedule 0.6.0

- Your own API secrets and tokens.


## Final Notes

- You can use this code for your personal Twitter bot, modify it, add new stuff, but first read the LICENSE to avoid Copyright problems.

- My twitter @Sgewux it's open to all of you and of course you can follow and interact with @HowManyWeeksBot.

- If you go to the first  project's commits you will see my old API tokens and secrets, I'm not dumb, I've regenated them and now these old tokens and keys are just trash so don't try to use them.
