from unisdk.sms import UniSMS
from unisdk.exception import UniException

def example():
  client = UniSMS("your access key id", "your access key secret")

  try:
    res = client.send({
      "to": "your phone number",
      "signature": "UniSMS",
      "templateId": "login_tmpl",
      "templateData": {
        "code": 7777
      }
    })
    print(res)
  except UniException as e:
    print(e)

if __name__ == '__main__':
    example()
