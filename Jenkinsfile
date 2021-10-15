node {
    dir ('jenkins-test') { // clone 받은 프로젝트 안의 jenkins-test 디렉토리에서 stage 실행
        stage ('jenkins-test/aws-ubuntu.pkr.hcl') {
            sh 'packer init .'
            sh 'packer build aws-ubuntu.pkr.hcl'
        }
    }
}
