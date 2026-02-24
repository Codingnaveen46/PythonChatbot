pipeline {
    agent any

    environment {
        IMAGE_NAME = "opsnaveen/opsnaveen-python-chatbot:${GIT_COMMIT}"
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Codingnaveen46/PythonChatbot.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "Building Docker Image..."
                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-hub-cred',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                    echo "Pushing Docker Image to Docker Hub..."
                    docker push ${IMAGE_NAME}
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    echo "Cleaning any running container..."
                    docker rm -f opsnaveen-python-chatbot || true

                    echo "Starting new container..."
                    docker run -d --name opsnaveen-python-chatbot -p 9001:8501 ${IMAGE_NAME}
                '''
            }
        }
    }
}