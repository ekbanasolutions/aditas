# Aditas Server

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Deployment](#deployment)
- [Built with](#built-with)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install and how to install them

```
* Apache2

You can install the above libraries using the following command

    sudo apt-get update
    sudo apt-get install apache2

```

## Deployment

This section discuss about how to deploy this application on live system with debian package in ubuntu server.

- Step 1: Create a file 'aditas_server.list' as follows.
```
echo "deb [arch=amd64] http://aditasapt.ekbana.net/repo/apt/server xenial main" | sudo tee /etc/apt/sources.list.d/aditas_server.list
```

- Step 2: Update Ubuntu services and install the debian package of Aditas

```
sudo apt-get update
sudo apt-get install aditas-server
```

Follow the installation process

- Step 3: Goto /usr/share/aditas/server/ and copy 'aditas_server.conf' to apache2, sites-available location.
```
Example:
    sudo cp /usr/share/aditas/server/aditas_server.conf /etc/apache2/sites-available/
```
- Step 4: Enable aditas site for apache2
```
cd /etc/apache2/sites-available
sudo a2ensite aditas_server.conf
sudo service apache2 restart (Restart Apache2)
```

- Step 5: Finally

Goto browser and check if ip_address:port site is working
```
ip_address: refers to your system ip address.
port: default is 11600
```
## Built With

* [Django](https://docs.djangoproject.com/en/2.1/) - Web framework used


