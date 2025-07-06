// Jenkinfile
// Declarative pipeline

pipeline{
    agent any
    environment{
        // Define your Docker image name and tag
        FLASK_APP_IMAGE = "my-flask-app:${env.BUILD_NUMBER}"
        // If pushing to Docker Hub or a private registry, add variables here:
        // DOCKER_REGISTRY = "your-dockerhub-username"
        // DOCKER_CREDENTIAL_ID = "dockerhub-credentials" // Jenkins credential ID for Docker Hub
    }

    stages{
        stage('Checkout Code'){
            steps{
                git branch: 'main', url: 'https://github.com/iammmarah/jenkinstest.git'
                // Replace 'main' with your branch and 'your-username/your-flask-app.git' with your repo URL
                // If your repo is private, you'll need to set up Jenkins credentials for Git.
            }
        }
        stage('Build Docker Image'){
            steps{
                script{
                    // Build docker image
                    sh "docker build -t ${env.FLASK_APP_IMAGE}"
                    echo "Docker image ${env.FLASK_APP_IMAGE} built successfully."
                }
            }
        }
        stage('Stop and Remove Old Container (if exists)') {
            steps {
                script {
                    // Stop and remove any old running container with the same name
                    sh "docker stop my-flask-app-container || true" // || true to prevent build failure if container doesn't exist
                    sh "docker rm my-flask-app-container || true"
                }
            }
        }
        
        stage('Run New Docker Container') {
            steps {
                script {
                    // Run the new Docker container, mapping port 5000 to the host's 6100
                    // You might want to use a reverse proxy like Nginx or Caddy on your EC2 for production.
                    sh "docker run -d --name my-flask-app-container -p 6100:5000 ${env.FLASK_APP_IMAGE}"
                    echo "Flask app deployed and running on port 6100."
                }
            }
        }





    }

}