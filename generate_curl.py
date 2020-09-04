import json
import sys

def generate_curl(path, method, headers, body):
  headers_list = list()
  for k, v in headers.items():
    headers_list.append('-H \'%s: %s\' \\\n' % (k, v))
  command = 'curl -X %s %s \\\n%s-d \'%s\' | python -mjson.tool' % (method, path, ''.join(headers_list), json.dumps(body, indent=2, ensure_ascii=False))
  sys.stdout.buffer.write(command.encode('utf-8'))
