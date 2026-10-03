
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'py -m venv .venv-ci'
                bat '.venv-ci\\Scripts\\python -m pip install --upgrade pip'
                bat '.venv-ci\\Scripts\\python -m pip install -r requirements.txt'
                bat '.venv-ci\\Scripts\\playwright install chromium'
            }
        }

        stage('Run UI Tests') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat '.venv-ci\\Scripts\\python -m pytest -v --browser chromium --html=reports/test-report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/test-report.html',
                             allowEmptyArchive: true
        }
    }
}