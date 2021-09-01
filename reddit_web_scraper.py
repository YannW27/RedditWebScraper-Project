import praw
import os
import re


def reddit_web_scraper():
    input("Welcome to a Reddit web scraper, press enter to continue:")
    reddit = praw.Reddit(client_id=input("Please enter your client ID:"),
                         client_secret=input("Please enter your client secret:"),
                         user_agent=input("Please enter your user agent:"))
    subreddit = reddit.subreddit(input("Please write the name of the subreddit:"))
    subreddit_type_choice = input(
        'Please type in one of the following for the subsequent inquiries in the subreddit - hot, top, new :')
    if subreddit_type_choice == 'hot':
        posts_choice = subreddit.hot(limit=int(input('Please limit the number of inquiries(max 75):')))
    elif subreddit_type_choice == 'top':
        posts_choice = subreddit.top(limit=int(input('Please limit the number of inquiries(max 75):')))
    elif subreddit_type_choice == 'new':
        posts_choice = subreddit.new(limit=int(input('Please limit the number of inquiries(max 75):')))
    else:
        print('Error - please type in one of the three options ')

    parent_dir = "C:/Users/Public/Downloads"
    print("The dir path is set to C:/Users/Public/Downloads , it can be manually changed at the string parent_dir\n"
          "Please wait for the process to finish..")
    path = os.path.join(parent_dir, subreddit.display_name)
    os.mkdir(path)

    for post in posts_choice:
        directory = post.title
        directory = re.sub('[^A-Za-z0-9]+', ' ', directory)
        path_post = os.path.join(path, directory)
        os.mkdir(path_post)
        os.chdir(path_post)
        path_post = path_post.replace(os.sep, '/')
        PostContent = 'PostContent.txt'
        comments_content = 'Comments.txt'
        id_of_subreddit = post.id
        submission = reddit.submission(id=id_of_subreddit)
        self_text = [post.title, post.selftext, post.url, post.id]
        with open(PostContent, 'a+', encoding='cp850', errors='replace') as PostFile:
            data1 = PostFile.writelines('OP - ' + str(self_text) + '\n')
        PostFile.close()
        for comment in submission.comments:
            with open(comments_content, 'a+', encoding='cp850', errors='replace') as comments_file:
                data2 = comments_file.writelines('Commenter - ' + str(comment.author) + ':' +
                                                 '\n' + '"' + str(comment.body) + '\n' + '"' + '\n')
            comments_file.close()
