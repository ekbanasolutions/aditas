# Aditas Agent

- [Getting Started](#getting-started)
- [Deployment](#deployment)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development. See deployment for notes on how to deploy the project on a live system.

## Deployment

This section discuss about how to deploy this application on live system with debian package in ubuntu server.

- Step 1: Add GPG-Key for Aditas
```
wget -qO - http://aditasapt.ekbana.net/GPG-KEY-aditas | sudo apt-key add -
```

- Step 2: Create a file 'aditas_agent.list' as follows.
```
echo "deb [arch=amd64] http://aditasapt.ekbana.net/repo/apt/agent xenial main" | sudo tee /etc/apt/sources.list.d/aditas_agent.list
```

- Step 3: Update Ubuntu services and install the debian package of Aditas

```
sudo apt-get update
sudo apt-get install aditas-agent
```

Follow the installation process

- Step 4: Start Aditas Agent Service
```
/usr/share/aditas/agent/bin/aditas-agent start

You can also add aditas-agent bin directory to your bash script and directly run the agent using,
aditas-agent start/stop/restart
```

- Step 5: Finally

Goto browser and check if ip_address:port site is working
```
ip_address: refers to your system ip address.
port: default is 11605
if it is not working then check your log and see which port is it using.
```


