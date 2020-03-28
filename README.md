# Laravel Homestead Docker

## Load Docker image

### download
    https://drive.google.com/open?id=197UalIe-jSZ4tfE2AWyPeoFBdaukwjo6

### run command 
    docker load -i docker/homestead.tgz

## Docker work

### Start homestead

    docker-compose up -d

### Stop homestead

    docker-compose down 

### View log

    docker-compose logs -f

## Add new site

    1. Install fresh laravel project inside "workspace-www" dir

    2. Run "sudo ./update_hosts.py"
