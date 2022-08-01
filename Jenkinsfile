pipeline {
    agent { docker { image 'python:3.10.5-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'echo $PATH'
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install pymongo'
                }
            }
        }
        stage('test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python socket_stuff.py'
                }
            }
        }
        stage('deploy') {
            steps {
                echo 'pipeline passed'
            }
        }
    }
}