# Use an official Node runtime as a parent image
FROM node:16

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json into the container at /app
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files from the current directory into the container at /app
COPY . .

# Make port 3000 available for the app to use
EXPOSE 3000

# Define environment variable
ENV REACT_APP_API_URL=http://backend:8000

# Start the app
CMD ["npm", "start"]
