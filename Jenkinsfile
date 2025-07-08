pipeline {
    agent { 
        docker {
            image 'docker:dind'
            args '--privileged --network host -e DOCKER_TLS_CERTDIR=""'
            // --network host simplifies networking
            // Disabling TLS for simplicity in testing
        }
    }

    environment {
        REPO_URL = 'https://github.com/iammmarah/jenkinstest.git'
        IMAGE_NAME = 'flask-app-image'
        CONTAINER_NAME = 'flask-app'
    }

    stages {
        stage('Initialize Docker') {
            steps {
                script {
                    // Wait for Docker daemon to be ready
                    sh '''
                        while ! docker info >/dev/null 2>&1; do 
                            echo "Waiting for Docker daemon...";
                            sleep 1; 
                        done
                    '''
                }
            }
        }

        stage('Checkout Code') {
            steps {
                git url: "${REPO_URL}", branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Stop Existing Container') {
            steps {
                sh 'docker stop ${CONTAINER_NAME} || true'
                sh 'docker rm ${CONTAINER_NAME} || true'
            }
        }

        stage('Run Flask Container') {
            steps {
                sh 'docker run -d --name ${CONTAINER_NAME} -p 6100:5000 ${IMAGE_NAME}'
            }
        }
    }
}