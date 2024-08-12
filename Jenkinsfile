pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                git url: 'https://github.com/saksham0197/jenkins_Test.git', branch: 'main'
            }
        }
        
        // stage('Install Dependencies') {
        //     steps {
        //         // Install dependencies using pip
        //         sh 'pip install -r requirements.txt'
        //     }
        // }
        
        stage('Run Python Script') {
            steps {
                // Run the Python script
                sh 'python nexus.py'
            }
        }
        
        stage('Nexus IQ Scan') {
            steps {
                // Perform Nexus IQ scan on the code
                nexusPolicyEvaluation(
                    failBuildOnNetworkError: true, 
                    iqApplication: 'your-app-id',  // Replace with your Nexus IQ application ID
                    iqScanPatterns: '**/*.py',    // Pattern to scan Python files
                    iqStage: 'build'              // Nexus IQ stage, e.g., build
                )
            }
        }
    }
    
    post {
        always {
            // Clean up workspace after build
            cleanWs()
        }
    }
}
