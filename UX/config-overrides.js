const { override, addLessLoader, fixBabelImports, addWebpackAlias } = require('customize-cra')

const path = require("path")

module.exports = override(
  fixBabelImports('import', [
    {
      "libraryName": "@material-ui/core",
      "libraryDirectory": "components",
      "camel2DashComponentName": false,
    },
    {
      "libraryName": "@material-ui/icons",
      "libraryDirectory": "components",
      "camel2DashComponentName": false,
    },
  ]),
  addLessLoader(),
  addWebpackAlias({
    ["@"]: path.resolve(__dirname, "src")
  }),
);
