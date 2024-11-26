const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    //Para commit:
    // baseUrl: "https://projetomanguetown-app.azurewebsites.net",
    //Para testes locais:
    baseUrl: 'http://localhost:8000',
    viewportWidth: 1920,
    viewportHeight: 1080,
    watchForFileChanges: false,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});