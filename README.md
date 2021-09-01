Welcome to a web scraping project for Reddit using its API on Python using PyCharm IDE, 

To activate it correctly, you should prepare the 3 necessary keys,
to get access to Reddit API according to its rules.

You will be prompt to enter them one at a time, without any backslashes or
commas, quotation marks etc.

Simply enter them and press enter.

Should one of them be inputted incorrectly, the program will not work,
here is a link that explains how you can create them easily: 
https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c

For example:

client id: DvykV8SrI8HvQ6F6YJG5R
client secret: yaNe3ToNLb8IxHiyN06OsBhKtI5YWQ
user agent: WebScraping

Then you will be prompt to enter the name of the subreddit (without backslash) that you wish to scrape.

Then you will be prompt to select and write one of the 3 choices for the inquiries in the subreddit:
(hot, top, new)

Then you will be prompt to enter the limit number of inquiries, it is set to max 75 currently,
according to Reddit API rules. 
You could attempt to cross the 100/200 it might alter over time, 
I would begin with 5-20 inquiries to get the gist of it.

A Folder with the title of the subreddit will be created at this dir:
C:/Users/Public/Downloads/'subreddits name' (can be changed at your convenience)

In there, a folder will be created, having the title of the post as its name. (exectued for each post)

Then 2 files will be created in each post folder:
1. PostContent.txt - contains the post title, selftext, url, id (can add or subtract any more items at will)
2. Comments.txt - contains the comments author and body (can add or subtract any more items at will)

Wait for it to finish, and enjoy your data.



