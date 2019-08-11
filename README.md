# BevChill

Open terminal on laptop

### Start server
```python
cd server
python server.py
```

Look for the line 
```python
MY IP ADDRESS:
```

##### Copy the IP ADDRESS




### Start client
Open ANOTHER terminal with first still running

_SSH into your pi_

Start client to collect and send data
```python
cd client
python chill.py [server_ip] [type_in_test_file.csv]
```

Open http://\*server_ip\*:5000/ on web to view dashboard
