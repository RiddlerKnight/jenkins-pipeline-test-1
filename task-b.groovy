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
                sh """
                    #!/bin/bash
                    cat <<EOF > Doxyfile
                    PROJECT_NAME        = "GRPC"
                    INPUT               = "./src"
                    OUTPUT_DIRECTORY    = "out"
                    GENERATE_HTML       = "YES"
                    GENERATE_LATEX      = "NO"
                    RECURSIVE           = YES
                    FILE_PATTERNS       = *
                    """

                sh "doxygen Doxyfile"
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
