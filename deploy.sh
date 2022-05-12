export DOCKER="sudo docker-compose"
${DOCKER} down
sudo rm -rf backend/db/
sudo rm -rf backend/build/

git pull

${DOCKER} up --build -d
sleep 40

${DOCKER} exec backend initialize_db production.ini