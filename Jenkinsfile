// Jenkinsfile

// Define a declarative pipeline
pipeline {
    // Agent specifies where the pipeline will run.
    // 'any' means Jenkins will allocate an available agent.
    agent any

    // Environment variables that will be used throughout the pipeline.
    environment {
        // Replace 'YOUR_DOCKERHUB_USERNAME' with your Docker Hub username.
        DOCKERHUB_USERNAME = 'YOUR_DOCKERHUB_USERNAME'
        // Replace 'your-flask-app' with your desired Docker image name.
        IMAGE_NAME = 'your-flask-app'
        // Replace 'your-ec2-user@your-ec2-public-ip' with your EC2 instance connection string.
        // E.g., 'ubuntu@ec2-XXX-XXX-XXX-XXX.compute-1.amazonaws.com'
        EC2_HOST = 'your-ec2-user@your-ec2-public-ip'
        // Jenkins credential ID for SSH access to EC2.
        // This should be configured in Jenkins under 'Credentials'.
        EC2_SSH_CREDENTIALS_ID = 'ec2-ssh-key' // Example: 'my-ec2-ssh-key'
    }

    // Stages define the sequential steps of your pipeline.
    stages {
        // Stage 1: Build the Docker image
        stage('Build Docker Image') {
            steps {
                script {
                    // Print a message indicating the start of the build process.
                    echo "Building Docker image: ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}"
                    // Build the Docker image.
                    // -t: Tag the image with username/imagename:buildnumber (e.g., myuser/my-flask-app:1)
                    // .: Build context is the current directory.
                    sh "docker build -t ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER} ."
                    // Also tag it as 'latest' for easy reference.
                    sh "docker tag ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER} ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest"
                }
            }
        }

        // Stage 2: Push the Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                script {
                    // Print a message indicating the start of the push process.
                    echo "Pushing Docker image: ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER} and latest"
                    // Use 'withCredentials' to securely access Docker Hub credentials stored in Jenkins.
                    // 'dockerhub-credentials' should be the ID of your 'Username with password' credential in Jenkins.
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Log in to Docker Hub using the credentials.
                        sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin"
                        // Push the tagged image.
                        sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:${BUILD_NUMBER}"
                        // Push the 'latest' tagged image.
                        sh "docker push ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }

        // Stage 3: Deploy the Docker image to AWS EC2
        stage('Deploy to EC2') {
            steps {
                script {
                    // Print a message indicating the start of the deployment process.
                    echo "Deploying to EC2 instance: ${EC2_HOST}"
                    // Use 'sshagent' to securely use the SSH key credential for connecting to EC2.
                    // This assumes you have the 'SSH Agent' plugin installed in Jenkins.
                    sshagent(credentials: [EC2_SSH_CREDENTIALS_ID]) {
                        // Connect to the EC2 instance and execute commands remotely.
                        // 1. Stop and remove any existing container running the Flask app.
                        // 2. Pull the latest Docker image from Docker Hub.
                        // 3. Run the new Docker image, mapping container port 5000 to host port 80.
                        //    -d: run in detached mode
                        //    --rm: automatically remove the container when it exits
                        //    -p 80:5000: map host port 80 to container port 5000
                        //    --name: assign a name to the container for easier management
                        sh """
                            ssh -o StrictHostKeyChecking=no ${EC2_HOST} "
                                docker stop ${IMAGE_NAME} || true && docker rm ${IMAGE_NAME} || true
                                docker pull ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest
                                docker run -d --rm -p 80:5000 --name ${IMAGE_NAME} ${DOCKERHUB_USERNAME}/${IMAGE_NAME}:latest
                            "
                        """
                    }
                }
            }
        }
    }

    // Post-build actions: executed after all stages are complete.
    post {
        // Always block: executed regardless of the pipeline's success or failure.
        always {
            // Clean up the workspace after the build.
            deleteDir()
        }
        // Success block: executed only if the pipeline succeeds.
        success {
            echo 'Pipeline successfully completed!'
        }
        // Failure block: executed only if the pipeline fails.
        failure {
            echo 'Pipeline failed!'
        }
    }
}
