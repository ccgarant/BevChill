# BevChill

### Start server

Open terminal on laptop

```python
cd server
python server.py
```

Look for the line 
```python
MY IP ADDRESS:
```

##### Copy the IP ADDRESS

- - -


### Start client
Open ANOTHER terminal with first still running

##### SSH into your pi

Start client to collect and send data
```python
cd client
python chill.py [server_ip] [type_in_test_file.csv]
```

- - -

### View data

Open http://\*MY IP ADDRESS\*:5000/ on web to view live data
