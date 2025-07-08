pipeline {
    agent any  // Run initial stages on any agent
    
    environment {
        REPO_URL = 'https://github.com/iammmarah/jenkinstest.git'
        IMAGE_NAME = 'flask-app-image'
        CONTAINER_NAME = 'flask-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: "${REPO_URL}", branch: 'main'
            }
        }

        stage('Build and Run') {
            agent {
                docker {
                    image 'docker:latest'  // Official Docker CLI image
                    args '-v /var/run/docker.sock:/var/run/docker.sock -u root'
                    // Mounts host's Docker socket and runs as root
                }
            }
            steps {
                script {
                    // Verify Docker connectivity
                    sh 'docker ps >/dev/null && echo "Docker is working" || echo "Docker failed"'
                    
                    // Build the image
                    sh 'docker build -t ${IMAGE_NAME} .'
                    
                    // Stop and remove existing container
                    sh 'docker stop ${CONTAINER_NAME} || true'
                    sh 'docker rm ${CONTAINER_NAME} || true'
                    
                    // Run new container
                    sh 'docker run -d --name ${CONTAINER_NAME} -p 6100:5000 ${IMAGE_NAME}'
                }
            }
        }
    }
}