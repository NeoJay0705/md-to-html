# Markdown To HTML
This tool is used for transferring a markdown format to an HTML format.

The core of the tool uses GitHub API, which requests with a markdown content to the GitHub server and returns a response with the HTML content.

But in the response there lack `<body>` tag to decorate the page.

So, I add the important tags with the response. The tags are stored in `./resource/template/pattern`.

# How to
Follow the two steps to get a beautiful document:

First, put your markdown file into `./resource`

Second, open a terminal and execute `python -m mdtohtml.loader ./resource/<markdown-file-name>`

The HTML format file is stored in `./layout` with the same file name.