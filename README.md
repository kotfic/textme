# TextMe
Just a little wrapper around email/sms gateways provided by most cellular companies.  I happen to use vtext.com
(http://www.verizonwireless.com/support/vtext-website-faqs/)

These variables must be defined in your environment (eg. .bashrc)
```bash
export TEXTME_TO_EMAIL=[user@vtext.com]
export TEXTME_FROM_EMAIL=[user@gmail.com]
export TEXTME_PASSWORD=[*******]
```

## Usage

```bash
$>  ./long_process; textme "Process complete!" 
```

From python
```python
from textme import textme

def main():
   # Long running process here
   
if __name__ == "__main__":
try:
    main()
    textme("Grid Search complete", subject="i2b2")
except Exception, e:
    textme("Grid search crashed with {}".format(e.message), subject="i2b2")
    raise

```
