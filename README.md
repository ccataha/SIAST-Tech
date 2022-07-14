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
git clone https://github.com/farazahmadkhan15/NIDS_APP.git 
cd NIDS_APP 
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
Установка и удаление через setup.py
sudo python setup.py install --record files.txt
# inspect files.txt to make sure it looks ok. Then:
tr '\n' '\0' < files.txt | xargs -0 sudo rm -f --

If you have problems with requests module:
* grant you have local cicflowmeter pyenv 2.7.18
install requests lib through apt install 
* do: sudo su 
. venv/bin/activate
flask run
* if you have problems with libpcap, do: apt install -y libpcap0.8
flask run

db configure:
*sudo apt install postgresql postgresql-contrib
*sudo -u postgres psql
*postgres-# create database SIAST_USERS
*postgres-# create user siast_user with passsword 'ninja'
*postgres-# alter role siast_user set client_encoding to 'utf8'
*postgres-# alter role siast_user set default_transaction_isolation TO 'read committed'
*postgres-# alter role siast_user set timezone to 'UTC'
*postgres-# grant all privileges on database SIAST_USERS to siast_user

