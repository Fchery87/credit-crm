# Set the base image
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Install dependencies
COPY apps/web/package*.json ./
RUN npm install

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the application
CMD ["npm", "run", "dev"]
