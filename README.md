# SensorsData
                                                            
This API is built using Python's flask package to store information coming in from RPIs to sqlite database which is used by 'Daily Reporting app' to show information on website.

---

### Flow of the application:
<img src="https://github.com/sakshi-seth-17/SensorsData/blob/main/SensorDataFlow.jpg" alt="Alt text" title="Optional title">

### Instructions
1. Clone this repository. \
`git clone https://github.com/sakshi-seth-17/SensorsData.git`

2. Make neccessary changes required in the app.py wrt specific path. 

3. Travel to the parent project directory and install the required python packages. \
Create virtual environment – `python3 -m venv venv` \
`source venv/bin/activate` \
`pip3 install -r requirement.txt` \
To check if application is working fine run – `python3 app.py` 

### API listing on webserver
1. To access any API from outside the server, the API needs to be listed on the server.
2. Steps to register the API on the server with reverse proxy:
  - First, allow outgoing port - sudo ufw allow 8071
  - sudo ufw enable
  - sudo ufw status
  - cd /etc/apache2/sites-available
  - sudo nano 000-default.conf
    o	Add below lines \
    		#SensorsData  \
    		ProxyPass /database  http://128.192.158.63:8071/database  \
    		ProxyPassReverse /database  http://128.192.158.63:8071/database   
  - Now restart apache2
    `sudo systemctl restart apache2` 
    `sudo systemctl status apache2` 
    

### Create service file to make the app run indefinitely
`sudo nano /lib/systemd/system/SensorsData.service` \
Paste below lines inside the file by making necessary changes 

		[Unit] 
		Description=Sensor Data Management 
		After=multi-user.target 

		[Service] 
		User=webserver 
		Type=idle 
		ExecStart=/var/www/aspendb/probesearch/SensorsData/venv/bin/python3 /var/www/aspendb/probesearch/SensorsData/app.py 
		Restart=on-failure 


		[Install] 
		WantedBy=multi-user.target 

`sudo chmod 644 /lib/systemd/system/SensorsData.service` \
`sudo systemctl enable SensorsData.service` \
`sudo systemctl daemon-reload` \
`sudo systemctl start SensorsData.service` \
`sudo systemctl status SensorsData.service` 

---
### Location details of the components:
1.	Application code path (on webserver - webserver@128.192.158.63) path: /var/www/aspendb/probesearch/SensorsData
2.	Centralized Local database (on webserver - webserver@128.192.158.63) path: /var/www/aspendb/probesearch/SensorsData


---
### Technical details:
1. The application is built using Python.
2. The application runs on port 8071

---
### Folder Structure
- venv/
- Data-Store.db (Not on github because the file is large)
- app.py
- userdefined.py
- requirement.txt
	
