pipeline {
  agent any
  parameters {
    choice(name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: '')
    booleanParam(name: 'executeTests', defaultValue: true, description: '')
  }
  stages {
    stage("build") {
      steps {
        echo 'building the app ... an update...'
      }
    }
    
    stage("test") {
      when {
        expression {
          params.executeTests
        }
      }
      steps {
        echo 'testing the app ...'
      }
    }
    
    stage("deploy") {
      steps {
        echo 'deploying the app ...'
        echo "deploying version ${params.VERSION}"
      }
    }
    
  }
}
