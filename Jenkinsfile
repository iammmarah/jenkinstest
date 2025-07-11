pipeline {
    agent any
    environment {
        IMAGE_NAME = "test/flask-app" // Replace 'test' with your Docker Hub username if pushing
        CONTAINER_NAME = "flask-app"
        // REGISTRY_CREDENTIAL = 'dockerhub-cred' // Uncomment if pushing to Docker Hub
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/iammmarah/jenkinstest.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build image with build number and tag as latest
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                    sh "docker tag ${IMAGE_NAME}:${env.BUILD_NUMBER} ${IMAGE_NAME}:latest"
                }
            }
        }
        // Optional: Uncomment if pushing to Docker Hub
        /*
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', env.REGISTRY_CREDENTIAL) {
                        dockerImage.push("${env.BUILD_NUMBER}")
                        dockerImage.push('latest')
                    }
                }
            }
        }
        */
        stage('Run Container') {
            steps {
                script {
                    // Stop and remove existing container to avoid conflicts
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                    // Run the new container
                    sh "docker run -d -p 6100:6100 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
                }
            }
        }
        stage('Clean Up') {
            steps {
                // Remove old images
                sh "docker rmi ${IMAGE_NAME}:${env.BUILD_NUMBER} || true"
            }
        }
    }
    // post {
    //     always {
    //         // Clean up container on success or failure
    //         sh "docker stop ${CONTAINER_NAME} || true"
    //         sh "docker rm ${CONTAINER_NAME} || true"
    //     }
    // }
}