pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install --user pymongo'
                sh 'python3 add_plant.py'
            }
        }
    }
}