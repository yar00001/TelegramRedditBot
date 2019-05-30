from setuptools import setup, find_packages

setup(
    name='TelegramRedditBot',
    version='0.1dev',
    description='Reddit Wrapper for Telegram',
    author='H.H.Yar',
    author_email='hooman.yar@gmail.com',
    packages=find_packages(),
    install_requires=['praw', 'python-telegram-bot'],  # external packages as dependencies
)
