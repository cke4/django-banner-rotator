#-*- coding:utf-8 -*-

from random import random

from django.db import models


def pick(bias_list):
    """ Takes a list of 2-tuples [(item, weight)] using weight as the
        probability when calculating an item to choose
    """
    try:
        # First, normalize weights to ensure we
        # have a valid probability distribution
        assert sum([w for i, w in bias_list]) == 1
    except AssertionError:
        norm_const = float(sum([w for i, w in bias_list]))
        distribution = [(i, w / norm_const) for i, w in bias_list]
    else:
        distribution = bias_list

    number = random()
    current = 0.0

    # @link http://fr.w3support.net/index.php?db=so&id=479236
    for choice, probability in distribution:
        current += probability
        if number <= current:
            return choice


class BannerManager(models.Manager):

    def biased_choice(self, place):
        max_views = models.F('max_views')
        max_clicks = models.F('max_clicks')
        filter = {'is_active': True, 'places': place}
        
        if max_views > 0:
            filter['views__lt'] = max_views
        if max_clicks > 0:
            filter['click_count__lt'] = max_clicks
            
        queryset = self.filter(**filter)

        if not queryset.count():
            raise self.model.DoesNotExist

        normalizer = queryset.aggregate(normalizer=models.Sum('weight'))['normalizer']
        return pick([(i, i.weight / float(normalizer)) for i in queryset])
