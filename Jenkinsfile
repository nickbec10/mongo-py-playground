pipeline {
    agent { docker { image 'python:3.10.5-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
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