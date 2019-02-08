## Bogazici University Registiration Bot

### Requirements
- [Requests](http://docs.python-requests.org/en/master/)
  `pip3 install requests`
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  `pip3 install beautifulsoup4`

### Usage
```python
    # Create instance
    reg = Registration(STUDENT_ID, STUDENT_PASSWORD)
    
    # Set debug true for printing logs to console
    reg.set_debug(True)
    
    # Get quota for HUM102.01
    reg.get_quota("HUM", "102", 11)

    # If login your account is successful
    if reg.login():
        # Take CMPE493.01 course
        reg.take_course("CMPE", "493", "01")
        
        # Try to change HTR312 section 11 to 14
        for i in range(11,15):
            reg.change_section("HTR", "312", i)
```
