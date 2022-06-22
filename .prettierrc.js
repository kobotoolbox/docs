{
module.exports = {
  trailingComma: 'es5',
  tabWidth: 2,
  tabs: false,
  semi: true,
  singleQuote: true,
  quoteProps: 'as-needed',
  jsxSingleQuote: true,
  bracketSpacing: false,
  jsxBracketSameLine: false,
  arrowParens: 'always',
  endOfLine: 'lf',
  overrides: [
    {
      files: 'source/*.md',
      options: {
        parser: 'markdown',
        printWidth: 80,
        proseWrap: 'always'
      }
    }
  ]
};

}
