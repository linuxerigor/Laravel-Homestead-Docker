
### conectar ao mysql denrto do docker
    mysql -h127.0.0.1 -P3306  -uroot -p

### rodando container limpo do alpine

    docker run -it --name webserver -d alpine

### instalando pacotes necessarios para o Laravel
    apk add nginx vim php7 php7-bcmath php7-ctype php7-fileinfo php7-json php7-mbstring php7-xmlwriter  php7-dom php7-openssl php7-pdo_mysql php7-tokenizer php7-xml php7-fpm tzdata openrc php70-session composer --no-cache

### acerto do timezone
    TIMEZONE="America/Sao_Paulo"
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime
    echo "${TIMEZONE}" > /etc/timezone
    sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php7/php.ini

### criar a imagem no docker
    docker commit -a "Igor Marques"  d2607d8fc1f0 igor-homestead

### exportar para o tgz
