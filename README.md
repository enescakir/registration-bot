## Bogazici University Registiration Bot

### Requirements
- [Requests](http://docs.python-requests.org/en/master/)
  `pip3 install requests`
<!-- - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  `pip3 install beautifulsoup4` -->

### Usage
```python
    reg = Registration(STUDENT_ID, STUDENT_PASSWORD)
    reg.set_debug(True)
    reg.login():
    reg.take_course("CMPE", "493", "01")
    for i in range(11,15):
        reg.change_section("HTR", "312", i)
```
