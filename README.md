# Triad Food Hardship
Node.js/express app for visualizing food deserts and the options for eleminating them.

## Getting it running
1. Run `git clone https://github.com/codeforgso/triad-food-hardship` and then `cd triad-food-hardship`
2. Make sure node.js is installed
	- Run `node --version`. You should see something like `v0.12.4`.
	- If you don't get an output, you can install Node at [nodejs.org](https://nodejs.org/download/)
3. Make sure grunt is installed
	- Run `grunt --version`. You should see something like `grunt-cli v0.1.13`.
	- If you don't get an output, you can [get started here](http://gruntjs.com/getting-started)
4. Run `npm install` to get the dependencies
5. Run `grunt` to start the web server
6. Navigate to `localhost:3000` in a web browser to view the application

## Notes
- grunt will restart the server any time a change is made outside of `/public` or `/views` directories
- Manually kill the server with `Ctrl-c`