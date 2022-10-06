# Real Time Network Intrusion Detection System Using Machine Learning
# В работе
```sh
cd cicflowmeter
sudo python3 setup.py install 
```
### net-tools
```sh
sudo apt install net-tools
```
### whois
```sh
sudo apt install whois
```
### Redis-server
```sh
sudo apt update
sudo apt install redis-server
```
To start Redis Server
```sh
 sudo service redis-server start
```
To check status
```sh
 sudo service redis-server status
```
## Installing Application: 
```sh
git clone https://github.com/koidula/SIAST-Tech.git 
cd SIAST-Tech
python3 -m venv venv 
. venv/bin/activate 
 pip install -r requirements.txt 
```
## Running App
```sh
sudo su 
. venv/bin/activate 
flask run
```



