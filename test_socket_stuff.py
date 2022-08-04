import socket_stuff

def test_dns1():
    output = socket_stuff.check_dns("atomictinker.com")
    assert output == True

def test_dns2():
    output = socket_stuff.check_dns("google.com")
    assert output == True

# def test_dns3():
#     output = socket_stuff.check_dns("bcnisacubkaw3u.com")
#     assert output == True

def test_ntp1():
    output = socket_stuff.check_ntp("132.163.4.103")
    assert output == 'NTP is up'

def test_ntp2():
    output = socket_stuff.check_ntp("6.5.6.5")
    assert output == 'NTP is up'

def test_web1():
    output = socket_stuff.check_web("stackoverflow.com")
    assert output == True

def test_web2():
    output = socket_stuff.check_web("www.wunderground.com")
    assert output == True

# def test_web3():
#     output = socket_stuff.check_web("jkbcvskue.com")
#     assert output == True