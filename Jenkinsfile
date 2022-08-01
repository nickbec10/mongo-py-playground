pipeline {
    agent { docker { image 'python:3.10.5-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'echo $PATH'
                sh 'python --version'
                sh 'pip install paramiko'
                sh 'virtualenv venv && . venv/bin/activate && pip install pymongo'
            }
        }
        stage('test') {
            steps {
                sh 'python add_plant.py'
            }
        }
        stage('deploy') {
            steps {
                echo 'pipeline passed'
            }
        }
    }
}