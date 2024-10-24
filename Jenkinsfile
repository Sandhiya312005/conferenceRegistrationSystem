pipeline {
    agent any
    triggers {
        githubPush() // Trigger on GitHub push events
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies directly
                sh 'pip install django' // Replace with your specific packages
                // Add other necessary packages here, e.g., 'pip install djangorestframework'
            }
        }
        stage('Migrate') {
            steps {
                // Run database migrations
                sh 'python manage.py migrate'
            }
        }
        stage('Test') {
            steps {
                // Run tests
                sh 'python manage.py test'
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
