# Use a base image with Miniconda installed
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the environment.yml file
COPY environment.yml .

# Create the Conda environment
RUN conda env create -f environment.yml

# Activate the environment and install additional packages if necessary
RUN echo "source activate myenv" > ~/.bashrc
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# Copy the rest of the application code
COPY . .

# Run the application
CMD ["python", "app.py"]
