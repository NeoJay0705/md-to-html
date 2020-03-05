import sys
import re
import time
from .githubapi import MdtoHtml

class Loader:
    def __init__(self):
        super().__init__()
        self.api = MdtoHtml.createAPI()

    def md2html(self, mdText: str=None) -> str:
        """
        Return a HTML content based on input, `mdText`, or from a markdown file

        If you don't input `mdText`, you must assign a file when you execute 
        the loader class.
        """
        if mdText == None:
            try:
                with open(sys.argv[1], 'r', encoding='utf-8') as mdFile:
                    self.api.updateMarkdownContent(mdFile.read())
                    githubHTML = self.api.getMd2htl()
            except:
                raise Exception("File Not Found")
        else:
            self.api.updateMarkdownContent(mdText)
            githubHTML = self.api.getMd2htl()
        
        return githubHTML

    def export(self):
        """
        Export a HTML file to the relative path `./layout/` with the same name
        defined in the relative path `./resource/`

        The base HTML patter are stored in the relative path `./resource/template/pattern`.
        """
        githubHTML = self.md2html()

        with open('./resource/template/pattern', 'r') as pattern:
            with open('./layout/' + re.search(r'([^/]+)\.md$'
                , sys.argv[1]).group(1) + '.html', 'w') as layout:
                result = re.sub(r'{{htmlCode}}', githubHTML, pattern.read())
                layout.write(result)

if __name__ == '__main__':
    start_time = time.time()

    loader = Loader()
    loader.export()

    print("Executive time: ", time.time() - start_time)