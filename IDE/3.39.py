facebook = input('Has Facebook account? (y/n): ') == 'y'
twitter = input('Has Twitter account? (y/n): ') == 'y'
instagram = input('Has Instagram account? (y/n): ') == 'y'

count = sum([facebook, twitter, instagram])
if count >= 2:
    print('You are a good influencer!')
else:
    print('Not quite a top influencer yet.')