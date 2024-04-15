FROM node:18-alpine

WORKDIR /app


RUN yarn

COPY . .

EXPOSE 3000

CMD [ "yarn", "start" ]
# or
# CMD [ "npm", "start" ]