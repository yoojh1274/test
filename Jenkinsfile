node {
    dir ('jenkins-test') { // clone 받은 프로젝트 안의 jenkins-test 디렉토리에서 stage 실행
        stage ('jenkins-test/aws-ubuntu.pkr.hcl') {
            sh 'export AWS_ACCESS_KEY_ID=AKIAQKLMKUXXBF7BUDE2'
            sh 'export AWS_SECRET_ACCESS_KEY=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'
            sh 'packer init .'
            sh 'packer build aws-ubuntu.pkr.hcl'
        }
    }
}
