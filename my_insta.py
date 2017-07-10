import requests
#access token for performing operation on user and owner account<<<<< used in the scope of basic, public_content, likes, comments.>>>>>
access_token = "2313244363.1677ed0.e608298b62c44a84b2db85a26cb4d688"

base_url = "https://api.instagram.com/v1"


def self_info():                      #getting the collection of user
    url = base_url + "/users/self/?access_token=" + access_token
    my_info = requests.get(url).json()
    print my_info
    print my_info["data"]["full_name"]
    print my_info["data"]["profile_picture"]
    print my_info["data"]["bio"]
    print my_info["data"]["counts"]["followed_by"]
    print my_info["data"]["counts"]["follows"]


# https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN

def user_search(user_name):                #get user id
    if user_name not in ['shafiqur.raghib', 'kunal_pathak21']:
        print"you enter wrong username"
        return
    else:

         url_user = base_url + "/users/search?q=" + user_name + "&access_token=" + access_token
         print url_user
        # https://api.instagram.com/v1/users/search?q=jack&access_token=ACCESS-TOKEN
         user_detail = requests.get(url_user).json()
         success = user_detail["meta"]["code"]
         if success == 200:
               print "user detail found"
               print"the insta_username is :" + user_detail['data'][0]['full_name']
         else:
               print "user detail not found plz try again"
         return user_detail["data"][0]["id"]
                  # returning user id
         # print user_info['data'][0]['profile_picture']
        #user_search("amritbirsingh345")

def latest_post(user_name):
    user_id = user_search(user_name)
    url_user = base_url + "/users/" + str(user_id) + "/media/recent/?access_token=" + access_token

    # https://api.instagram.com/v1/users/{user-id}/media/recent/?access_token=ACCESS-TOKEN
    latest_post = requests.get(url_user).json()
    print "latest post entered by user is:" + latest_post["data"][0]["link"]
    return latest_post["data"][0]["id"]

#it is for making the like on te user id
def like_user_post(user_name):
    post_id = latest_post(user_name)
    payload = {"access_token": access_token}
    request_url = base_url + "/media/" + post_id + "/likes"
    response_to_like = requests.post(request_url, payload).json()
    if response_to_like['meta']['code'] == 200:
        print ("pic has been liked")
        # print response_to_like
    else:
        print("Something went wrong! Please do it again")

#it is for making the comment on user id
def comment_user_post(user_name):
    post_id = latest_post(user_name)
    request_url = (base_url + "/media/%s/comments?access_token=%s") % (post_id, access_token)
    request = requests.post(request_url).json()
    if request['meta']['code'] == 200:
        print("comment added ")
        print request  ["data"]["text"]
    else:
        print("comment not added try again")
     #return request["data"]["id"]

#for searching the comment
def search_comments(user_name):
    post_id = latest_post(user_name)
    request_url = base_url + "/media/" + post_id + "/comments?access_token=" + access_token
    request_comment = requests.get(request_url).json()
    return request_comment["data"][0]["id"]
        # print request_comment["data"][0]["text"]

#for deleting the comment
def delete_comment(user_name):
    post_id = latest_post(user_name)
    comment_id = comment_user_post(user_name)
    request_url = base_url + "/media/" + post_id + "/comments/" + comment_id + "?access_token=" + access_token
    request_comment = requests.delete(request_url).json()
    if request_comment['meta']['code'] == 200:
        print("your comment is deleted")
        # print comments
    else:
        print("Some error occurred! Try Again.")
        print request_comment

print("\nHello User! Welcome to the Instabot Environment.")
choice = 1
while choice != '9':
    print("\nWhat do you want to do using the Instabot?")
    print("1. Information of user")
    print("2. Get the name of user.")
    print("3. Recent post of the user.")
    print("4. Like a post of the user.")
    print("5. Comment on post of the user.")
    print("6. Delete the comment containing a particular word.")
    print("7. Exit.\n\n")

    choice = input("Enter Your Choice(1-9) : ")   #choose the number you want

    user_name = raw_input("Enter the following users 1.shafiqur.raghib 2.kunal_pathak21")

        # Perform Actions Depending on the User's Choice. Runs Until User wishes to Exit.
        # if choice in ['1', '2', '3', '4', '5', '6', '7']:
    if int(choice) == 1:
        self_info()

    elif int(choice) == 2:
        user_search(user_name)

    elif int(choice) == 3:
        latest_post(user_name)


    elif int(choice) == 4:
        like_user_post(user_name)

    elif int(choice) == 5:
        comment_user_post(user_name)

    elif int(choice) == 7:
        delete_comment(user_name)

    else:
        print('Exit')
