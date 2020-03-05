import http.client
import json
from . import apiConfig
from abc import ABCMeta, abstractmethod

class GitHubAPI(metaclass=ABCMeta):
    @abstractmethod
    def callAPI(self) -> http.client.HTTPResponse:
        pass

class MdtoHtml(GitHubAPI):
    def __init__(self, markdownContent: str=None):
        super().__init__()
        self.__matchProtocal()
        self.__markdownContent = markdownContent

    @staticmethod
    def createAPI():
        """
        Return a GitHubAPI instance
        """
        return MdtoHtml()

    def updateMarkdownContent(self, markdownContent: str) -> None:
        self.__markdownContent = markdownContent

    def __matchProtocal(self) -> None:
        if apiConfig.serverInfo["port"] == 443:
            self.connection = http.client.HTTPSConnection(
                apiConfig.serverInfo["host"])
        else:
            raise Exception("Unknown port")

    def getMd2htl(self) -> str:
        """
        Return a HTML code with utf-8 format when status code is 200.
        
        Before using this function, you can update markdown content by calling
        the function, udateMarkdownContent(markdownContent).
        
        If the return code is'nt 200, the function throw exception and what error server
        send.
        """
        response = self.callAPI()

        if response.status == 200:
            return response.read().decode("utf-8")
        else:
            raise Exception(
                "{} {}\n{}".format(
                      response.status
                    , response.reason
                    , response.read()))

    def callAPI(self) -> http.client.HTTPResponse:
        """
        Return a HTTPResponse object

        You can use all of the response content yourself.
        """
        payload = apiConfig.payload

        if self.__markdownContent != None:
            payload["text"] = self.__markdownContent

        jsonPayload = json.dumps(payload)
        
        try:
            self.connection.request(
                  'POST'
                , apiConfig.serverInfo["basepath"]["markdown"]
                , jsonPayload
                , apiConfig.header)
        
            return self.connection.getresponse()
        except:
            raise Exception("Connection error")

if __name__ == '__main__':
    markdownContent = "# Hello World\n This is a test!"

    api = MdtoHtml(markdownContent=markdownContent)
    
    print(api.getMd2htl())
