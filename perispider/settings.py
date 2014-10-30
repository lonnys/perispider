# -*- coding: utf-8 -*-

# Scrapy settings for perispider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'perispider'
DOWNLOAD_DELAY = 2
SPIDER_MODULES = ['perispider.spiders']
NEWSPIDER_MODULE = 'perispider.spiders'
ITEM_PIPELINES = ["perispider.pipelines.PerispiderPipeline"]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
