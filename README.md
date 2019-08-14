# BevChill

### Start server

Open terminal on laptop

```bash
cd server
python server.py
```

Look for the line 
```bash
MY IP ADDRESS:
```

##### Copy the IP ADDRESS

- - -


### Start client
Open ANOTHER terminal with first still running

SSH into your pi using [GNU Screen](https://www.linode.com/docs/networking/ssh/using-gnu-screen-to-manage-persistent-terminal-sessions/)
```bash
ssh -t pi@<pi_ip_addresss> screen -r
```

Start client to collect and send data
```bash
cd client
python chill.py -i <MY IP ADDRESS> -o <type_in_test_file.csv>
```
_-i := server ip_

_-o := output file name_

- - -

### View data

Open http://\*MY IP ADDRESS\*:5000/ on web to view live data

- - -

### End Screen 

Ctrl+a d

Ctrl+c
