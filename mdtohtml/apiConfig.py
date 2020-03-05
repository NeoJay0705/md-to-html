# GitHub API server information
serverInfo = {
    "host": "api.github.com",
    "port": 443,
    "basepath": {
        "markdown": "/markdown"
    }
}

# Http request header
header = {
    'Content-Type': 'application/json',
    'User-Agent': 'Neo'
}

# The contents can reference to GitHub developer website:
# https://developer.github.com/v3/markdown/#render-an-arbitrary-markdown-document
payload = {
    "text": "Please assign a markdown file to `md2html` function!",
    "mode": "gfm",
    "context": "github/gollum"
}