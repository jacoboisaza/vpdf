import eslint from "@eslint/js";
import eslintPrettier from "eslint-config-prettier";
import eslintPluginPrettierVue from "eslint-plugin-prettier-vue";
import eslintPluginVue from "eslint-plugin-vue";
import globals from "globals";

/**
 * Eslint configuration options.
 * @typedef {Object} EslintConfig
 * @property {Object} languageOptions - Language options for eslint.
 * @property {Object} eslintConfig - Recommended eslint configuration.
 * @property {Object} eslintPrettier - Eslint prettier configuration.
 * @property {Object} plugins - Eslint plugins.
 * @property {Object} eslintPluginVue - Eslint plugin for Vue.
 * @property {Object} eslintPluginPrettierVue - Eslint plugin for prettier Vue.
 */

/**
 * Eslint configuration array.
 * @type {EslintConfig[]}
 */
export default [
  {
    languageOptions: { globals: globals.browser },
  },
  eslint.configs.recommended,
  eslintPrettier,
  {
    plugins: {
      eslintPluginVue: eslintPluginVue,
      eslintPluginPrettierVue: eslintPluginPrettierVue,
    },
  },
  // override/add rules settings here
  {
    rules: {
      quotes: ["error", "single"],
    },
  },
];
