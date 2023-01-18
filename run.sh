docker build . -t security_lab_robot_scanner --no-cache
docker run -v $(pwd)/results:/outputs security_lab_robot_scanner 80
