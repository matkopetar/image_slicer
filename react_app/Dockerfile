FROM node:13.12.0-alpine

WORKDIR /
ADD ./ /

ENV PATH /react_app/node_modules/.bin:$PATH

RUN cd react_app
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

WORKDIR /react_app
CMD ["npm", "start"]

