import os
from unittest import TestCase

from src import config


class TestJon(TestCase):

    def test_one(self):
        season_four = os.path.join(config.NBA_MATCHES_DIR, '2003-2004')


