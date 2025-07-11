pipeline {
    agent any
    environment {
        IMAGE_NAME = "test/flask-app"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/iammmarah/jenkinstest.git', branch: 'main',
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Run Container') {
            steps {
                sh "docker run -d -p 6100:6100 --name flask-app ${IMAGE_NAME}:latest"
            }
        }

    }
}