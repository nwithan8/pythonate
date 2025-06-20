from urllib.parse import urlencode

import python8.uuid as general
import python8.web.requests as requests


def _make_google_analytics_url(params_dict):
    base_url = "https://www.google-analytics.com/collect"
    args = urlencode(params_dict)
    return f"{base_url}?{args}"


class GoogleAnalytics:
    def __init__(self,
                 analytics_id: str,
                 anonymous_ip: bool = False,
                 do_not_track: bool = False):
        """
        :param analytics_id: Your Google Analytics ID
        :type analytics_id: str
        :param anonymous_ip: If True, the IP address will be anonymized
        :type anonymous_ip: bool
        :param do_not_track: If True, the user will not be tracked
        :type do_not_track: bool
        """
        self.analytics_id = analytics_id
        self.version = '1'
        self.anonymize_ip = anonymous_ip
        self.do_not_track = do_not_track

    def _send(self, final_params) -> bool:
        if self.do_not_track:
            return True
        url = _make_google_analytics_url(params_dict=final_params)
        if requests.post(url=url):
            return True
        return False

    def event(self,
              event_category: str,
              event_action: str,
              event_label: str = None,
              event_value: int = None,
              user_id: str = None,
              anonymize_ip: bool = False,
              random_uuid_if_needed: bool = False) -> bool:
        """
        Log an event to Google Analytics
        :param event_category: The category of the event
        :type event_category: str
        :param event_action: The action of the event
        :type event_action: str
        :param event_label: The label of the event
        :type event_label: str
        :param event_value: The value of the event
        :type event_value: int
        :param user_id: The user ID of the event
        :type user_id: str
        :param anonymize_ip: If True, the IP address will be anonymized
        :type anonymize_ip: bool
        :param random_uuid_if_needed: If True, the user ID will be generated
        :type random_uuid_if_needed: bool
        :return: True if the event was sent successfully, False otherwise
        :rtype: bool
        """
        if self.do_not_track:
            return True
        if not user_id:
            user_id = str(general.generate_uuid(use_random=random_uuid_if_needed))
        final_params = {'v': self.version, 'tid': self.analytics_id, 't': 'event', 'cid': user_id}
        if anonymize_ip or self.anonymize_ip:
            final_params['aip'] = 0
        final_params['ec'] = event_category
        final_params['ea'] = event_action
        if event_label:
            final_params['el'] = event_label
        if event_value:
            final_params['ev'] = event_value
        return self._send(final_params=final_params)

    def page_view(self,
                  visited_page: str,
                  page_title: str = None,
                  user_id: str = None,
                  anonymize_ip: bool = False,
                  random_uuid_if_needed: bool = False) -> bool:
        """
        Log a page view to Google Analytics
        :param visited_page: The URL of the page
        :type visited_page: str
        :param page_title: The title of the page
        :type page_title: str
        :param user_id: The user ID of the page view
        :type user_id: str
        :param anonymize_ip: If True, the IP address will be anonymized
        :type anonymize_ip: bool
        :param random_uuid_if_needed: If True, the user ID will be generated
        :type random_uuid_if_needed: bool
        :return: True if the page view was sent successfully, False otherwise
        :rtype: bool
        """
        if self.do_not_track:
            return True
        if not user_id:
            user_id = str(general.generate_uuid(use_random=random_uuid_if_needed))
        final_params = {'v': self.version, 'tid': self.analytics_id, 't': 'pageview', 'cid': user_id}
        if anonymize_ip or self.anonymize_ip:
            final_params['aip'] = 0
        if not visited_page.startswith('/'):
            visited_page = f"/{visited_page}"
        final_params['dl'] = visited_page
        if page_title:
            final_params['dt'] = page_title
        return self._send(final_params=final_params)
