import os
import shutil
import unittest

import src.account as account
import src.detection as detection
import src.timing as timing

class DogTests(unittest.TestCase):
    timestamp_path = 'tmp/timestamp'

    def setUp(self):
        if not os.path.exists('tmp'):
            os.mkdir('tmp')

    def tearDown(self):
        shutil.rmtree('tmp')

    # Tests the detection of messages that should be responded to
    def testHotwordDetection(self):
        def assertHotcount(text, count):
            self.assertEqual(detection.hotword_count(text), count)

        # Standard cases

        assertHotcount("", 0)
        assertHotcount("here is some hotwordless text", 0)
        assertHotcount("trea t goo dd og", 0)
        assertHotcount("treat", 1)
        assertHotcount("good dog", 1)
        assertHotcount("Later I will go for a walk", 1)
        assertHotcount("On the walk I might get a treat for myself", 2)
        assertHotcount("I've been a good girl, so I will get a treat on my walk", 3)
        assertHotcount("walk walk walk walk walk walk walk", 7)

        # Punctuation

        assertHotcount("If you walk, get a treat.", 2)
        assertHotcount("I will treat, and then re-treat, myself.", 2)

        # Invalid formatting

        assertHotcount("I've been walking for hours", 0)
        assertHotcount("I have a boner", 0)
        assertHotcount("good     dog", 0)
        assertHotcount("t-reat", 0)

        # Corner cases

        assertHotcount("treatreatreat", 0)
        assertHotcount("ttttreatttt", 0)

    def testOptInOutDetection(self):
        def assertMentions(text, mentions):
            self.assertEqual(detection.mentions_handle(text, account.handle), mentions)

        def assertOptIn(text):
            self.assertTrue(detection.requests_start(text))

        def assertOptOut(text):
            self.assertTrue(detection.requests_stop(text))

        def assertNeither(text):
            self.assertFalse(detection.requests_start(text))
            self.assertFalse(detection.requests_stop(text))

        # Mentions

        assertMentions("@stock_photo_dog", True)
        assertMentions("@stock_photo_dog what's up my friend", True)
        assertMentions("stock_photo_dog words", False)
        assertMentions("Check out @stock_photo_dog", False)
        assertMentions("@stock_photo_dogs", False)
        assertMentions("@sstock_photo_dog", False)

        # Requests
        
        assertOptIn("@stock_photo_dog start")
        assertOptIn("@stock_photo_dog I would like to start interacting")
        assertOptOut("@stock_photo_dog stop")
        assertOptOut("@stock_photo_dog stop messaging me")
        assertNeither("@stock_photo_dog")
        assertNeither("@stock_photo_dog I don't like it")
        assertNeither("@stock_photo_dog good dog")


    def testTiming(self):
        timestamp = timing.get_iso_timestamp()
        timing.record_last_date(self.timestamp_path, timestamp)
        self.assertEqual(timestamp, timing.get_last_date(self.timestamp_path))
