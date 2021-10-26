# -*- coding: utf-8 -*-

from items import *

class ItemMapping(object):
    items = {
        "Aged Brie": AgedBrieItem,
        "Sulfuras, Hand of Ragnaros": SulfurasItem,
        "Backstage passes to a TAFKAL80ETC concert": BackStageItem,
        "Conjured": ConjuredItem
    }

    @classmethod
    def create(cls, item):
        if item.name in cls.items:
            return cls.items[item.name](item)
        return UpdateItem(item)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            itemMapping = ItemMapping.create(item)
            itemMapping.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
