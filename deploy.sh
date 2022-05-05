export DOCKER="sudo docker-compose"
${DOCKER} down
sudo rm -rf backend/bd_folder/
sudo rm -rf backend/build/

git pull

${DOCKER} build
${DOCKER} up -d
sleep 40

${DOCKER} exec backend initialize_db production.ini