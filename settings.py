# -*- coding: utf-8 -*-

# Scrapy settings for bbref project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bbref'

SPIDER_MODULES = ['bbref.spiders']
NEWSPIDER_MODULE = 'bbref.spiders'

DOWNLOAD_DELAY = 3

ITEM_PIPELINES = {'bbref.pipelines.BBrefPipeline': 100, }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbref (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = False


