FROM node:20-alpine AS base
WORKDIR /app

FROM base AS dependencies
COPY package*.json ./
RUN npm ci

FROM dependencies AS production
COPY src/ ./src/
COPY index.html vite.config.js ./
RUN npm run build

# Run as non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
