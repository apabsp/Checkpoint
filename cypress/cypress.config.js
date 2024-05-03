const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    //specPattern: '*.cy.js', // write your pattern here
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
