# Neural DevOps Autopilot

An intelligent DevOps automation platform that leverages generative AI and machine learning to predict anomalies, detect failures, and automatically generate remediation strategies for infrastructure and application deployment pipelines.

## Overview

Neural DevOps Autopilot is a comprehensive solution designed to streamline DevOps workflows through intelligent prediction and automated remediation. The system collects metrics from multiple sources, predicts potential failures using anomaly detection, and generates actionable pull requests to resolve identified issues.

## Features

- **Live Metrics Collection**: Integration with GitHub and other data sources for real-time performance monitoring
- **Predictive Failure Detection**: Machine learning-based anomaly detection to identify potential issues before they impact production
- **Automated Remediation**: Intelligent PR generation and deployment recommendations
- **Container Testing**: Comprehensive simulation suite for validating fixes in isolated environments
- **AI-Powered Analysis**: Integration with generative AI for intelligent insights and recommendations

## System Architecture

### Core Components

```
neural_devops_autopilot/
├── src/
│   ├── collectors/
│   │   └── github_metrics.py          # GitHub metrics collection
│   ├── prediction_engine/
│   │   └── anomaly_detector.py        # ML-based anomaly detection
│   ├── remediation_agent/
│   │   └── pr_generator.py            # Automated PR generation
│   └── simulation_suite/
│       └── container_tester.py        # Container-based testing
├── app.py                              # Streamlit web interface
└── requirements.txt                    # Python dependencies
```

## Prerequisites

- Python 3.8 or higher
- Docker (for container simulation tests)
- Git
- Valid API keys for:
  - GitHub API
  - Google Generative AI (Gemini)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Hasan393/AutoOps.git
cd AutoOps/neural_devops_autopilot
```

### 2. Set Up Environment

Create a copy of the environment template:

```bash
cp .env.example .env
```

Edit `.env` and populate with your credentials:

```dotenv
GOOGLE_API_KEY=your_google_api_key_here
GITHUB_TOKEN=your_github_token_here
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Start the Streamlit web interface:

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### Using Make Commands

The project includes a Makefile for common development tasks:

```bash
make install       # Install dependencies
make run          # Run the Streamlit application
make test         # Run test suite
make lint         # Run code quality checks
make format       # Format code with black
make clean        # Remove build artifacts
make help         # Display all available commands
```

## Development

### Project Structure

- **Collectors**: Modules for gathering metrics from external systems
  - `github_metrics.py`: Fetches repository and workflow metrics

- **Prediction Engine**: Machine learning components for anomaly detection
  - `anomaly_detector.py`: Detects failures using statistical analysis

- **Remediation Agent**: Automated fix generation
  - `pr_generator.py`: Creates pull requests with proposed fixes

- **Simulation Suite**: Testing and validation framework
  - `container_tester.py`: Validates fixes in containerized environments

### Code Standards

The project follows PEP 8 guidelines. Use the Makefile to maintain code quality:

```bash
make format  # Auto-format code
make lint    # Check code quality
```

## Configuration

All configuration is managed through environment variables in `.env`. Refer to `.env.example` for required variables and their descriptions.

### Required Variables

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | API key for Google Generative AI (Gemini) |
| `GITHUB_TOKEN` | GitHub personal access token for API requests |

## API Integration

### GitHub API

The metrics collector interfaces with GitHub's REST API to retrieve:
- Repository statistics
- Workflow runs
- Pull request data
- Issue history

### Google Generative AI

The system uses Gemini 2.5 Flash for:
- Anomaly analysis and interpretation
- Remediation strategy generation
- Root cause analysis

## Testing

Run the test suite:

```bash
make test
```

For container-based testing, ensure Docker is running:

```bash
python -m pytest src/simulation_suite/
```

## Troubleshooting

### Import Errors

Ensure the virtual environment is activated and dependencies are installed:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### API Authentication Failures

Verify that `.env` contains valid credentials:

```bash
cat .env
```

### Streamlit Port Already in Use

Specify an alternative port:

```bash
streamlit run app.py --server.port 8502
```

## Performance Considerations

- Metric collection occurs asynchronously to avoid blocking the UI
- Anomaly detection runs on batches for efficient processing
- Container simulation tests are rate-limited to prevent resource exhaustion

## Security

- Never commit `.env` files with real credentials
- Use GitHub's secret management for CI/CD pipelines
- Rotate API keys regularly
- Review generated pull requests before merging

## Contributing

Contributions are welcome. Please ensure:

1. Code follows PEP 8 standards
2. All tests pass: `make test`
3. Code is formatted: `make format`
4. Documentation is updated

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

## Roadmap

- Integration with additional cloud providers (AWS, GCP, Azure)
- Advanced ML models for failure prediction
- Custom remediation strategies
- Multi-environment orchestration
- Real-time alerting system

## Authors

Developed as part of the AutoOps initiative for intelligent DevOps automation.
