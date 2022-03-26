sudo docker image build -t docker_env .
sudo docker run -v /home/ito/work/docker-env:/workspace/docker_env -w /workspace/docker_env -it docker_env