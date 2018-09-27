# coding:utf-8

import requests
import json
import unittest
import ddt

class LoginTest(unittest.TestCase):
    '''
    登录测试
    '''
    url="http://183.62.96.187:8855/api/json"
    data = {
        "head": '{"appid":"KYTESTDRV","command":"StaffLogin","device_id":"F30000370000E1","encrypt_type":0,"sign":"66da9672e0ff00d2","token":"","version":"1.1"}',
        "body": '{"datainfo":null,"password":"a0b923820dcc509a","userno":"simon"}'
    }

    def test_login(self):
        print type(self.data)
        req = requests.post(url=self.url, data=self.data)
        code = req.json()['result_code']
        print code
        self.assertAlmostEqual(code, 0, u'登录失败')


if __name__ == '__main__':
    unittest.main()