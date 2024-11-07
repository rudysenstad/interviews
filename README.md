# Disney AI LLM Contractor via Milestone tech
## Design
1. The dataset is from RottenTomatoes found on the Kaggle dataset repository
2. The database design can be further optimized, but I wanted to highlight how I break a part one row into logical parts to allow for  maintainability and query performance. For example, one row can be broken down to people involved in the movie, movie details, review details, and genre/people types. This allows us to find all movies a certain actor or director is a part of. Or a particular category of movie.
3. I've chosen to load the pre-processed data into Postgres and then load embeddings into pinecone as a vector db.
4. The system design includes 5 containers: 2 indexes of pinecone, 1 postgres db, 1 ETL processor and 1 agent
5. The docker-compose makes it easy to spin up and run the system
6. Please note I took many shortcuts and did not do much of any error handling as I would do in productions
7. I've chosen to use OpenAI gpt-4o-mini for the generative output and the embeddings
8. I've chosen to use langchain to handle RAG using a SQL agent to pull data using similarity search since the requirements don't specify a need for human in the loop. If it did, the complexity would increase and I would consider using LangGraph.
9. ETL is running in a monolithic notebook. In production I would consider using Airflow or some orchestration tool to manage the process
## Setup
### Example documentation of setting up the system
- [Docker Install](https://docs.docker.com/desktop/)
- [Build a langchain Agent](https://www.docker.com/blog/build-and-deploy-a-langchain-powered-chat-app-with-docker-and-streamlit/)
- [Add RAG to langchain](https://python.langchain.com/docs/tutorials/rag/)
###
```
docker build -t stitch_etl:latest Dockerfile.ETL
docker build -t stitch_ai:latest Dockerfile.agent
docker-compose up -d
```
## Requirements
### Data Ingestion
Provide a dataset (e.g., JSON, CSV, or unstructured text files) that includes a mix of structured and
unstructured data. Ask the candidate to create a pipeline to load this data into a database of their
choice, ensuring the schema is optimized for querying.
### Data Preprocessing
The data may contain noise or require transformation (e.g., text cleaning, parsing nested JSON,
handling missing values). The candidate should demonstrate how they preprocess the data for
efficient storage and later retrieval.
### Vectorization
Using a pre-trained language model or embeddings model, ask the candidate to convert the
unstructured text into embeddings. Store these embeddings in a vector storage solution of their
choice, ensuring the pipeline can handle batch processing for larger datasets.
### Query and Retrieve
Create a simple API or script that allows querying based on a given text prompt. The query should
retrieve similar embeddings from the vector store and return the corresponding records from the
database. Include a use case for Retriever-Augmented Generation (RAG), where the retrieved data
is used to generate a summary or response based on the query.
### Documentation
The candidate should document their code, the thought process behind their design choices, and
any trade-offs they considered (e.g., schema design, vector storage approach, etc.)
### Bonus
Implement monitoring or logging for the data pipeline to track the data flow and identify potential
bottlenecks. Optimize the pipeline for scalability, such as handling larger files or parallel processing.