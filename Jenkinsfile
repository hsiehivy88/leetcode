pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        powershell(script: 'pipeline', returnStatus: true, returnStdout: true, encoding: 'node {      stage(\'Stage 1\'){        echo \'Hello World 1\'    }    stage(\'Stage 2\'){        echo \'Hello World 2\'    } }')
      }
    }
    stage('Stage 1') {
      parallel {
        stage('Stage 1') {
          steps {
            sh '''node {  
   stage(\'Stage 1\'){
       echo \'Hello World 1\'
   }
}'''
          }
        }
        stage('Stage 2') {
          steps {
            sh '''node {  
   stage(\'Stage 2\'){
       echo \'FXXXXXX\'
   }
}'''
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        mail(subject: 'test', body: 'hhahahahahah', to: 'ivy_hsieh@trend.com.tw')
      }
    }
  }
}