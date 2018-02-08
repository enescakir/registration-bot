## Bogazici University Registiration Bot

### Requirements
- [Requests](http://docs.python-requests.org/en/master/)
  `pip3 install requests`
<!-- - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  `pip3 install beautifulsoup4` -->

### Usage
```python
    reg = Registiration("STUDENT_ID", "STUDENT_PASSWORD")
    reg.setDebug(True)
    reg.login():
    reg.takeCourse("CMPE", "493", "01")
    for i in range(11,15):
        reg.changeSection("HTR", "312", i)
```
