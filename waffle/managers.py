from __future__ import absolute_import, unicode_literals

from django.db import models

from waffle.utils import get_setting, get_cache


cache = get_cache()


class BaseManager(models.Manager):
    KEY_SETTING = ''

    def create(self, *args, **kwargs):
        ret = super(BaseManager, self).create(*args, **kwargs)
        cache_key = get_setting(self.KEY_SETTING)
        cache.delete(cache_key)
        return ret


class FlagManager(BaseManager):
    KEY_SETTING = 'ALL_FLAGS_CACHE_KEY'


class SwitchManager(BaseManager):
    KEY_SETTING = 'ALL_SWITCHES_CACHE_KEY'


class SampleManager(BaseManager):
    KEY_SETTING = 'ALL_SAMPLES_CACHE_KEY'
