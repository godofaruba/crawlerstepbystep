import re

content = 'Hello 1234567 Word_This is a Regex Demo'
# 贪婪
result = re.match('^He.*(\d+).*Demo$', content)
# 非贪婪
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))