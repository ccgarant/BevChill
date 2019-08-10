# BevChill

Open terminal

### Start server
```python
cd server
python server.py
```
This will attempt to start a server at http://192.168.1.180:5000/

_If you get an error that it cannot start at this location run_
```python
ifconfig
```
_And look for an ip that starts with 192.168_
_Copy this and replace '192.168.1.180' in server.py and chill.py_ 


### Start client
Open ANOTHER terminal with first still running

Start client to collect and send data
```python
cd client
python chill.py [type_in_test_file.csv]
```

Open http://192.168.1.180:5000/ on web to view dashboard
