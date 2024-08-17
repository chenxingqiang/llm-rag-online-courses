# LLM-RAG Online Course

This repository contains the course materials and project structure for the LLM-RAG (Large Language Models and Retrieval-Augmented Generation) online course.

## Course Structure

The course is divided into two main phases:
1. Fundamentals of LLM
2. RAG Knowledge and Practice

Each phase contains multiple lessons, available as Jupyter notebooks in the `notebooks` directory.

## Getting Started

1. Clone this repository
2. Install the required dependencies: `pip install -r requirements.txt`
3. Navigate to the `notebooks` directory and start with `lesson1_course_overview.ipynb`

## Project Structure

- `notebooks/`: Contains all course lessons as Jupyter notebooks
- `src/`: Source code for the project
- `data/`: Data files used in the course
- `tests/`: Unit tests for the project
- `docs/`: Additional documentation
- `config/`: Configuration files
- `scripts/`: Utility scripts

## Docker

To run the project using Docker:

1. Build the Docker image: `docker build -t llm-rag-course .`
2. Run the container: `docker run -p 80:80 llm-rag-course`

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.