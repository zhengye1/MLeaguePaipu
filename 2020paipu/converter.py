import re

def trans_url(line):
    return re.sub(r'\[(?P<content>.*?)\]\((?P<url>[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?)\)',
                  '[url=\g<url>]\g<content>[/url]',
                  line)

if __name__ == 'main':
  print("Hello World")

  print(line)