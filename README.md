This application can be used in 3 ways

### Console App

``` powershell
$ python src/ConsoleApp.py 1 3 98
```

### Flask API
``` powershell
$ python src/FlaskApi.py
```
It binds to the 0.0.0.0 and runs on default flask port 5000
Demo on a windows machine but will work on linux as well with curl - 
``` powershell
$ Invoke-RestMethod -ContentType "application/json" -Method Put  http://localhost:5000/sum -Body '{[2, 3, 4]}'
```

### Docker container

Build the container
``` powershell
$ docker build .\src\ -f .\src\DockerFile -t tvarit/sumof3
$ docker run -p 5000:5000 tvarit/sumof3
```

To get the ip on which the api can be accessed, find which adapter docker is using.
``` powershell
$ ipconfig
```
Will give you the list of adapters. Find the one which is begin used by docker. It would have docker in its name or in my case WSL

```
Ethernet adapter vEthernet (WSL):

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::bd66:e641:22ae:ef77%55
   IPv4 Address. . . . . . . . . . . : 172.29.160.1
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
```
Use the IP of the above adapter to query deployed API
``` powershell
$ Invoke-RestMethod -ContentType "application/json" -Method Put  http://172.29.160.1:5000/sum -Body '{[2, 3, 14]}'
$ 5
```