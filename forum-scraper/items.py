# -*- coding: utf-8 -*-

#
# Represents the message and relevant fields
from scrapy import Item, Field

class ForumMessageItem(Item):
    message = Field()
    author = Field()
    author_post_count = Field()
    
