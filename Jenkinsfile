pipeline {
    agent any

    environment {
        IMAGE_NAME = "opsnaveen/opsnaveen-python-chatbot:${GIT_COMMIT}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Codingnaveen46/PythonChatbot.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    echo "Building Docker Image"
                    docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker rm -f opsnaveen-python-chatbot || true
                    docker run -d --name opsnaveen-python-chatbot -p 9001:8501 ${IMAGE_NAME}
                '''
            }
        }
    }
}

#test