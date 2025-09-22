pipeline {
    agent {
        label 'doxygen-agent'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'git@github.com:RiddlerKnight/grpc.git',
                    credentialsId: 'rk-gh'
            }
        }
        stage('Doxygen') {
            steps {
                sh "doxygen Doxyfile"
                // echo "List file"
                // sh "ls -la"
                sh "tar -czvf doc.tar.gz out/html "
            }
        }
        stage('archive') {
            steps {
                archiveArtifacts artifacts: 'doc.tar.gz', fingerprint: true
            }
        }
    }
}
