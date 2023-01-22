from facebook_scraper import get_posts
import json
from getpass import getpass
print('Enter Profile ID:')
pro_id = input();
print('Enter your Email:')
em = input();
password = getpass()
posts = get_posts(pro_id, pages=4,credentials=(em,password),options={"comments":True})

for post in posts:
	with open('poc.json','a',encoding='utf-8') as f:
		json.dump(post,f,ensure_ascii=False,default=str)
		f.write("\n")
	print(post['post_text'])
	for cmt in post['comments_full']:
		print(cmt['commenter_name']," : ", cmt ['comment_text'].replace("\n",""))
