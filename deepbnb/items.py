# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DeepbnbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    access = scrapy.Field()
    additional_house_rules = scrapy.Field()
    allows_events = scrapy.Field()
    amenities = scrapy.Field()
    business_travel_ready = scrapy.Field()
    calendar_updated_at = scrapy.Field()
    city = scrapy.Field()
    description = scrapy.Field()
    host_id = scrapy.Field()
    id = scrapy.Field()
    interaction = scrapy.Field()
    is_hotel = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    min_nights = scrapy.Field()
    monthly_price_factor = scrapy.Field()
    name = scrapy.Field()
    neighborhood_overview = scrapy.Field()
    notes = scrapy.Field()
    person_capacity = scrapy.Field()
    price_rate = scrapy.Field()
    price_rate_type = scrapy.Field()
    rating_accuracy = scrapy.Field()
    rating_checkin = scrapy.Field()
    rating_cleanliness = scrapy.Field()
    rating_communication = scrapy.Field()
    rating_location = scrapy.Field()
    rating_value = scrapy.Field()
    response_rate = scrapy.Field()
    response_time = scrapy.Field()
    review_count = scrapy.Field()
    review_score = scrapy.Field()
    room_type = scrapy.Field()
    satisfaction_guest = scrapy.Field()
    star_rating = scrapy.Field()
    tier_id = scrapy.Field()
    total_price = scrapy.Field()
    url = scrapy.Field()
    user_id = scrapy.Field()
    weekly_price_factor = scrapy.Field()
