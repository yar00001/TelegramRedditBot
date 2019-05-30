from reddit_bot.reddit import reddit_instance_generator

# Reddit Read Only Instance - No Authentication is done
reddit_read_only = reddit_instance_generator.RedditInstance().get_read_only_instance()


def get_subreddit(subreddit_name):
    return reddit_read_only.subreddit(subreddit_name)


def get_n_hot_submissions(subreddit_name, limit_number):
    titles = []
    count = 0
    for submission in get_subreddit(subreddit_name).hot(limit=limit_number):
        # print('{} - {}'.format(count, submission.title))
        count += 1
        titles.append(submission.title)
    return titles


# Create a submission to /r/test
# reddit.subreddit('test').submit('Test Submission From AWS', url='https://reddit.com')

# Test
if __name__ == '__main__':
    get_n_hot_submissions('IAmA', 5)
else:
    print('{} is imported.'.format(__file__))