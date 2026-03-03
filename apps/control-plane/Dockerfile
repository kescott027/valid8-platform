FROM node:20-alpine

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

COPY tsconfig.json eslint.config.js ./
COPY src ./src
RUN npm run build

ENV NODE_ENV=production
EXPOSE 3000
CMD ["node", "dist/server.js"]
