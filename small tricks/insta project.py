import json
followeing  = open("following.json", 'r')
followers = open("followers.json", 'r')

following_json = json.lead(following)
followers_json = json.lead(followers)

def parse_json(json_file, str_):
  curr_set = set()
  for user in json_file(str_):
    curr_set_add(user['string_list_data'][0]['value'])
  return curr_set

set_following = parse_json(following_json, 'relationships_following') - parse_json(followers_json, 'relationships_followers')

for users_not_following in not_following:
  print(users_not_following)
