#!groovy

node {
  currentBuild.result = "SUCCESS"

  // https://www.quernus.co.uk/2016/10/03/wipe-workspace-jenkins-2.0-deletedir/
  deleteDir() // wipe the workspace

  try {
    stage('Checkout') {
      checkout scm
    }

    stage('Build HTML') {
      sh 'tox -e html'
    }

    // NOTE: replace this when ftp publish plugin supports pipelines
    stage('Archive files') {
      archiveArtifacts artifacts: 'build/html/**/*', fingerprint: true
    }
  }

  catch (err) {
    currentBuild.result = "FAILURE"
      throw err
  }
}
