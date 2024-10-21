const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "https://smartcapital-fdd8hfepc3ekdxez.brazilsouth-01.azurewebsites.net/",
    viewportWidth: 1920,
    viewportHeight: 1080,
    watchForFileChanges: false,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});