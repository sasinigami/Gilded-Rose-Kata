# -*- coding: utf-8 -*-

class UpdateItem(object):
    max_quality = 50

    def __init__(self, item):
        self.item = item

    def increase_quality(self):
        if self.item.quality < self.max_quality:
            self.item.quality = self.item.quality + 1

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

    def decrease_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def update_quality(self):
        self.decrease_quality()
        self.decrease_sell_in()

        if self.item.sell_in < 0:
            self.decrease_quality()


class AgedBrieItem(UpdateItem):
    def update_quality(self):
        self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.increase_quality()


class BackStageItem(UpdateItem):
    days_threshold_min = 10
    days_threshold_max = 5

    def reset_quality(self):
        self.item.quality = 0

    def update_quality(self):
        self.increase_quality()
        if self.item.sell_in <= self.days_threshold_min:
            self.increase_quality()
        if self.item.sell_in <= self.days_threshold_max:
            self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.reset_quality()


class SulfurasItem(UpdateItem):
    def update_quality(self):
        pass


class ConjuredItem(UpdateItem):
    def decrease_quality(self):
        UpdateItem.decrease_quality(self)
        UpdateItem.decrease_quality(self)
