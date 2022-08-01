pipeline {
    agent none
    stages {
        stage('build') {
            agent { docker { image 'python:3.10.5-alpine' } }
            steps {
                sh 'echo $PATH'
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install pymongo'
                }
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