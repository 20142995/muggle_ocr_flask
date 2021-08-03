FROM tensorflow/tensorflow
WORKDIR /app
ADD ./ /app
RUN  pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
RUN apt-get update && apt-get install -y libgl1-mesa-glx 
EXPOSE 5000
CMD ["python", "/app/server.py"]