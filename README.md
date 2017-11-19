# Sites Monitoring Utility
Checks the status of sites from the given file.

# Quick Start
Scipt should be run by Python3.5

Example of run on Linux

```bash
$python3 check_sites_health.py domains.txt
http://www.lenta.ru
    HTTP response status is 200: ok
    Domain prepaid one month ahead: ok
http://www.devman.org
    HTTP response status is 200: ok
    Domain prepaid one month ahead: ok
http://www.tut.by
    HTTP response status is 200: ok
    Expiry date cannot be estimated.
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
