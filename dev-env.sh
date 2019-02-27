HOST_IP=$(hostname -I | cut -d\  -f 1)
#HOST_IP=127.0.0.1


export PFT_WORKSPACE=$(pwd)

export PFT_DB_NAME=pft
export PFT_DB_USER=dbuser
export PFT_DB_PASS=dbpass
export PFT_DB_HOST=${HOST_IP}
export PFT_DB_PORT=10001
export PFT_API_PORT=10000

export PFT_ADMIN_SECRET=sec

env | grep PFT_ > .env
