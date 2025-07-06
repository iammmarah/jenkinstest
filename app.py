# app.py
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    A simple root endpoint that returns a greeting message.
    """
    return "Hello from Flask! This app is running inside a Docker container."

@app.route('/health')
def health_check():
    """
    A health check endpoint to verify the application is running.
    Returns a JSON response indicating the status.
    """
    return jsonify(status="healthy", message="Flask app is up and running!")

if __name__ == '__main__':
    # Run the Flask application on all available network interfaces (0.0.0.0)
    # and listen on port 5000. This is important for Docker container accessibility.
    app.run(debug=True, host='0.0.0.0', port=6789)



# docker push ammarah24/test-repository-docker-jenkins:tagname



# docker build -t yourusername/my-repo:latest .


# docker build -t ammarah24/test-repository-docker-jenkins:latest .
# docker push ammarah24/test-repository-docker-jenkins:latest



# docker pull ammarah24/test-repository-docker-jenkins:latest

# docker pull jenkins/jenkins:latest  

# docker network create jenkins    


# docker run --name jenkins --restart=on-failure --detach \
#   --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
#   --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
#   --publish 8181:8080 --publish 50011:50000 \
#   --volume jenkins-data:/var/jenkins_home \
#   --volume jenkins-docker-certs:/certs/client:ro \
#   jenkins/jenkins:jdk21 




  # docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
