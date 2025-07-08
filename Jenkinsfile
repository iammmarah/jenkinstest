pipeline {
    agent { 
        node {
            label 'docker-python-flask-agent'
            }
      }

    environment {
        REPO_URL = 'https://github.com/iammmarah/jenkinstest.git'
        // CREDENTIALS_ID = 'github-creds'   // ID from Jenkins credentials
        IMAGE_NAME = 'flask-app-image'
        CONTAINER_NAME = 'flask-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // git credentialsId: "${CREDENTIALS_ID}", url: "${REPO_URL}", branch: 'main'
                git  url: "${REPO_URL}", branch: 'main'

            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Stop Existing Container') {
            steps {
                sh 'docker rm -f ${CONTAINER_NAME} || true'
            }
        }

        stage('Run Flask Container') {
            steps {
                sh 'docker run -d --name ${CONTAINER_NAME} -p 6100:5000 ${IMAGE_NAME}'
            }
        }
    }
}
