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

        stage('UI Health Test') {
            steps {
                sh '''
                    echo "Starting temporary container for UI test..."
                    docker run -d --rm --name temp-ui-test -p 8501:8501 ${IMAGE_NAME}

                    echo "Waiting for Streamlit to start..."
                    sleep 8

                    echo "Checking UI accessibility..."
                    curl -f http://localhost:8501 > /dev/null

                    echo "UI is reachable."
                    
                    # Stop the temp container
                    docker stop temp-ui-test || true
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
                    docker rm -f opsnaveen-python-chatbot || true

                    docker run -d --name opsnaveen-python-chatbot -p 9001:8501 ${IMAGE_NAME}

                    echo "Deployment complete. Application running on port 9001."
                '''
            }
        }
    }
}