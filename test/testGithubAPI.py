import unittest
from mdtohtml import githubapi

class Test_GithubAPI(unittest.TestCase):
    api = githubapi.MdtoHtml.createAPI()
    
    def test_withNone(self):
        Test_GithubAPI.api.getMd2htl()
        self.assertEqual(Test_GithubAPI.api.callAPI().getcode(), 200)

    def test_withText(self):
        Test_GithubAPI.api.updateMarkdownContent('# Title')
        Test_GithubAPI.api.getMd2htl()
        self.assertEqual(Test_GithubAPI.api.callAPI().getcode(), 200)

    def test_withEmpty(self):
        Test_GithubAPI.api.updateMarkdownContent('')
        Test_GithubAPI.api.getMd2htl()
        self.assertEqual(Test_GithubAPI.api.callAPI().getcode(), 200)

if __name__ == '__main__':
    unittest.main()