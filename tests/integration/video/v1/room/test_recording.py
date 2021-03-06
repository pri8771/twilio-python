# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class RoomRecordingTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .recordings(sid="RTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings/RTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "processing",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T21:00:00Z",
                "date_deleted": "2015-07-30T22:00:00Z",
                "sid": "RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "source_sid": "MTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "size": 0,
                "type": "audio",
                "duration": 0,
                "container_format": "mka",
                "codec": "OPUS",
                "track_name": "A name",
                "offset": 10,
                "grouping_sids": {
                    "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                },
                "media_external_location": "https://my-super-duper-bucket.s3.amazonaws.com/my/path/",
                "encryption_key": "public_key",
                "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "media": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .recordings(sid="RTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .recordings.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "recordings": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "recordings"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .recordings.list()

        self.assertIsNotNone(actual)

    def test_read_results_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "recordings": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "completed",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T21:00:00Z",
                        "date_deleted": "2015-07-30T22:00:00Z",
                        "sid": "RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "source_sid": "MTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "size": 23,
                        "type": "audio",
                        "duration": 10,
                        "container_format": "mka",
                        "codec": "OPUS",
                        "track_name": "A name",
                        "offset": 10,
                        "grouping_sids": {
                            "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "participant_sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        },
                        "media_external_location": "https://my-super-duper-bucket.s3.amazonaws.com/my/path/",
                        "encryption_key": "public_key",
                        "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "media": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/RTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "recordings"
                }
            }
            '''
        ))

        actual = self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .recordings.list()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                .recordings(sid="RTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://video.twilio.com/v1/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings/RTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.video.v1.rooms(sid="RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .recordings(sid="RTXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
