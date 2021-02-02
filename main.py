import tweepy
import datetime
import time
import random
import schedule

#Tokens
api_key = 'F4TIkczr6nSLVWKteeB2YTeHK'
api_secret_key = 'rUvvGkT2PMKcbjg0NUxGoyp3B36NlMqPKzQ2F4Ky3RUM4lFHLV'
access_token = '1345045932962947073-hESgm0OX8MhJAxxG9fxBnO29UkJP5R'
access_token_secret = 'MihuK5mjsUgmKCIYG3ByZ8VYWRi8Fg8DTm9MayycjJlxS'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

my_api = tweepy.API(auth, wait_on_rate_limit= True)


class Poster:
	def __init__(self, api):
		self.api = api


	@staticmethod
	def howManyWeeks():
		'''This function will help us to get how many weeks left no finish the current year'''

		current_date = datetime.datetime.now()
		current_week = int(current_date.strftime('%W'))
		current_year = current_date.year
		weeks_to_finish = 52 - current_week

		if current_week != 46:

			return f'Just {weeks_to_finish} weeks to finish the {current_year}!'

		else:

			return f'Just {weeks_to_finish} weeks to finish the {current_year}! \nOr in Colombian words "Se vino diciembre hpta!"'


	def post(self):

		self.api.update_status(self.howManyWeeks())
		

class Replier:

	def __init__(self, api):
		self.api = api
		self.replies =(
			':v',
			':O',
			':(',
			':)',
			'When I find myself in times of trouble, Mother Mary comes to me.\nSpeaking words of wisdom, let it be...',
			'You never thought I\'d ever be Something you want, something you need...',
			'I\'m naming the voices in my head...',
			'Oh gloria inmarcesible Oh júbilo inmortal... ',
			'Do u know where i can buy some bitcoins?',
			'A prokaryotic cell is a type of cell that does not have a true nucleus or membrane-bound organelles.',
			'A prokaryotic cell is a type of cell that does not have a true nucleus or membrane-bound organelles.',
			'Wanna know how many weeks left to finish the curren year?',
			'How u doing parcero?'
			)


	def get_last_mention(self):
		''' This function return us a status object of the last mention'''
		last_mention = self.api.mentions_timeline(count=1) 
		
		return last_mention[0]


	def is_new_mention(self, mention):
		''' This function returns true if the mention that we passed as a parameter it's a different mention than the last one'''
		with open('last_mention_id.txt', 'r') as f:

			if f.readlines()[0] != mention.id_str:

				return True

			else:

				return False


	def is_not_reply(self, mention):
		'''This function will return true if the mention isn't a reply'''
		
		if mention.in_reply_to_status_id == None:

			return True

		else: 

			return False


	def update_id(self, mention):
		'''This function updates the las_mention_id document with the current las mention's id after answer and replied it'''
		with open('last_mention_id.txt', 'w') as f:

			f.write(mention.id_str)


	def reply_to_last_mention(self, mention):

		self.api.update_status(f'@{mention.user.screen_name} {random.choice(self.replies)}', in_reply_to_status_id= mention.id)


	def like_mention(self, mention):

		self.api.create_favorite(mention.id)


if __name__ == '__main__':


	replier = Replier(my_api)
	poster = Poster(my_api)
	schedule.every().wednesday.at('17:15').do(poster.post)

	while True:

		
		schedule.run_pending()
		
		mention = replier.get_last_mention()

		if replier.is_new_mention(mention) == True and replier.is_not_reply(mention) == True: #If it's a new mention and aint a reply

			replier.reply_to_last_mention(mention)
			replier.like_mention(mention)
			replier.update_id(mention)
	
		time.sleep(60)

