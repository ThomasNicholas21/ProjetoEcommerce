#!/bin/sh
# Ficará executando até que o postgres seja iniciado, verificando o HOST e a PORTA
# configurando nas variáveis de ambiente
while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  echo "🟡 Waiting for MySQL Database Startup ($MYSQL_HOST:$MYSQL_PORT) ..."
  sleep 2
done

echo "✅ MySQL Database Started Successfully ($MYSQL_HOST:$MYSQL_PORT)"