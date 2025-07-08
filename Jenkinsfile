pipeline {
    agent any
    
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
                    image 'docker:latest'
                    args '-v /var/run/docker.sock:/var/run/docker.sock -u root'
                }
            }
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
                sh 'docker stop ${CONTAINER_NAME} || true'
                sh 'docker rm ${CONTAINER_NAME} || true'
                sh 'docker run -d --name ${CONTAINER_NAME} -p 6100:5000 ${IMAGE_NAME}'
            }
        }
    }
}