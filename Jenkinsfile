pipeline {
    stage('build') {
        agent { docker { image 'python:3.10.1-alpine' } }
        steps {
            sh 'pip install pymongo'
            sh 'python3 add_plant.py'
        }
    }
}