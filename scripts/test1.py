# coding:utf-8

import requests
import unittest
import ddt


@ddt.ddt
class LoginTest(unittest.TestCase):
    url="http://183.62.96.187:8855/api/json"

    @ddt.file_data('login_tc.yml')
    @ddt.unpack
    def test_login(self,data,message_ass):
        print type(data)
        req = requests.post(url=self.url, data=data)
        # body = req.json()['body']
        # token = json.loads(body)['token']
        # print token
        message = req.json()['message']
        print req.text
        self.assertEqual(message, message_ass, '测试失败，状态码不是%s'%message_ass)


if __name__ == '__main__':
    unittest.main()