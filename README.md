# Triad Food Hardship
Node.js/express app for visualizing food deserts and the options for eleminating them.

## Getting it running
1. Clone the project and `cd` to the directory
2. Make sure node.js is installed
	- Run `node --version`. You should see something like `v0.12.4`.
	- If you don't get an output, you can install Node.js at [nodejs.org](https://nodejs.org/download/)
3. Run `npm install` to get the dependencies
4. Run `npm start` to start the web server
5. Navigate to `localhost:3000` to view

## Notes
- Any modifications outside of the `/public` or `/views` directories will require the server to be restarted. Press `Ctrl-c` to kill the server and run `npm start` to start it again. There are tools to automate this for you - see [nodemon](http://nodemon.io/)
