pipeline {
    agent any

    tools {
        python 'Python3'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {

                sh 'nohup . venv/bin/activate && python app.py > flask.log 2>&1 &'
                sleep 5
            }
        }

        stage('UI Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/ --html=report.html --self-contained-html'
            }
            post {
                always {
                    publishHTML([
                        reportDir: '.',
                        reportFiles: 'report.html',
                        reportName: 'UI Test Report'
                    ])
                }
            }
        }
    }

    post {
        always {
            sh 'pkill -f "python app.py" || true'
        }
        failure {
            echo 'Тесты не пройдены – конвейер остановлен'
        }
        success {
            echo 'Все тесты успешно пройдены'
        }
    }
}