FROM node:20-alpine AS base
WORKDIR /app

FROM base AS dependencies
COPY package*.json ./
RUN npm ci --only=production

FROM dependencies AS production
COPY src/ ./src/
COPY index.html vite.config.js ./
RUN npm run build

# Run as non-root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 3000
CMD ["npm", "run", "preview"]
