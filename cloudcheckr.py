import httplib2
import json
import urllib

from endpoints import endpoints

"""Python CloudCheckr API wrapper.

Note: SSL is currently disabled. This issue needs to be fixed.

Examples:
  Instantiate a connection object:

  >>> _conn = CloudCheckr('https://app.cloudcheckr.com/api/',
                          '<access_key>',
                          {'Content-Type': 'application/json'})

  Call endpoints by invoking methods listed in endpoints.py. For
  example, to list best practices, call:

  >>> _conn.get_best_practices()
"""

class CloudCheckr(object):
  """CloudCheckr __init__ method.

  Args:
    hostname (str): The hostname for the CloudCheckr API
      (https://app.cloudcheckr.com/api/).
    access_key (str): The access key for an individual or master account
      in CloudCheckr.
    headers (dict, optional): Additional headers to be sent to the HTTP
      request payload.
  """
  def __init__(self, hostname, access_key,
                     headers={'Content-Type': 'application/json'}):
    self.hostname = hostname.rstrip('/')
    self.access_key = access_key
    self.endpoints = endpoints
    self.headers = headers
    self.body = None

  def __getattr__(self, method):
    """Operator overload method.

    Args:
      method (function): The method to be called for querying the
        CloudCheckr API. Method names are located in the endpoints.py
        module, and are the keys of the `endpoints` dictionary object.

    Returns:
      function: callback method.

    Raises:
      AttributeError: If the method name (key) does not exist in the
        `endpoints` dictionary.
    """
    def callback(self, **kwargs):
      """callback method.

      Args:
        **kwargs: Arbitrary keyword arguments found in the `params` key
          of the `endpoints` dictionary.

      Returns:
        function: _request method.
      """
      endpoint = self.endpoints[method]
      path = endpoint['path']
      verb = endpoint['method']
      status = endpoint['status']
      url = self.hostname + path
      url += '?access_key=' + self.access_key
      for kw in kwargs:
        if kw not in endpoint['params']:
          raise ValueError(
            'Keyword argument(s) not valid. Valid arguments are: %s' %
            ', '.join(endpoint['params']))
      else:
        url += '&' + urllib.urlencode(kwargs)
      self.client = httplib2.Http('.cache',
                                  disable_ssl_certificate_validation=True)
      (response, content) = self.client.request(url,
                                                verb,
                                                body=self.body,
                                                headers=self.headers)
      return self._request(response, content, status)
    if method not in self.endpoints:
      raise AttributeError('%s() method does not exist.' % method)
    return callback.__get__(self)

  def _request(self, response, content, status):
    """Private method.

    Args:
      response (dict): The HTTP response returned from the server.
      content (dict): The content returned from the HTTP request.
      status (int): The status code returned from the HTTP request.

    Returns:
      dict: The deserialzed JSON object returned from the HTTP request.

    Raises:
      Exception: If the server does not return a response.
      Exception: If the expected `status` code does not match the status
        code `s` returned from the server.
    """
    if not response:
      raise Exception('The server did not return a response.')
    s = int(response.get('status', 0))
    if s != status:
      raise Exception('Expected status code %d, got %d' % (status, s))
    return json.loads(content)
