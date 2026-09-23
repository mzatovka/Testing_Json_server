FROM node:20-alpine
WORKDIR /app
RUN npm install -g json-server
RUN mkdir -p fixtures
EXPOSE 3000
CMD ["json-server", "--watch", "fixtures/db.json", "--host", "0.0.0.0", "--port", "3000"]
