const webfontsGenerator = require('@vusion/webfonts-generator');
const fs = require('fs');
const simpleGit = require('simple-git');

const kpiDirName = 'temp-kpi-clone';
const sourceDir = `${kpiDirName}/jsapp/svg-icons/`;
const destDir = `source/_static/kpi-icons`;

const git = simpleGit({
  baseDir: process.cwd(),
  binary: 'git',
  maxConcurrentProcesses: 6,
});

function generateIconsFromKpiFiles() {
  console.info('Reading files…');
  const files = [];
  const icons = [];
  fs.readdirSync(sourceDir).forEach((file) => {
    if (file.endsWith('.svg')) {
      files.push(`${sourceDir}${file}`);
      icons.push(file.replace('.svg', ''));
    }
  });
  console.info(`${files.length} icons found.`);

  console.info('Generating fonts…');
  webfontsGenerator(
    {
      files: files,
      dest: destDir,
      fontName: 'k-icons',
      cssFontsUrl: './',
      css: true,
      cssTemplate: `${kpiDirName}/jsapp/k-icons-css-template.hbs`,
      html: true,
      // NOTE: we are not using the KPI template here, as the snippet is a tiny
      // bit different (no JSX).
      htmlTemplate: `scripts/k-icons-html-template.hbs`,
      types: ['eot', 'svg', 'ttf', 'woff2', 'woff'],
      order: ['woff2', 'woff', 'ttf', 'eot', 'svg'],
      templateOptions: {
        classPrefix: 'k-icon-',
        baseSelector: '.k-icon',
        baseClassName: 'k-icon',
      },
      formatOptions: {
        svg: {
          fontStyle: 'normal',
          fontWeight: 'normal',
          fixedWidth: true,
          centerHorizontally: false,
          normalize: false,
          height: 10000,
          round: 0,
          descent: 0,
          ascent: 0,
        },
        ttf: {},
        woff2: {},
        woff: {},
        eot: {},
      },
    },
    function (error) {
      if (error) {
        throw new Error('Fail!', error);
      } else {
        try {
          console.info('Cleanup…');
          // Cleanup after everything is done.
          fs.rm(kpiDirName, {recursive: true}, (err) => {
            if (err) {
              throw err;
            }
            console.info('Icons generated successfully!');
          });
        } catch(e){
          console.warn(
            '\x1b[31m***\n',
            e,
            '\n***',
            '\x1b[0m'
          );
        }
      }
    }
  );
}

function getKpiFiles() {
  console.info("Cloning kpi repository…")
  // We clone the `kpi` repository to ensure we have the same set of icons <3.
  git.clone('https://github.com/kobotoolbox/kpi', kpiDirName, {
    '--single-branch': true,
    '--depth': 1,
  }).then(generateIconsFromKpiFiles)
}

function start() {
  if(fs.existsSync(kpiDirName)) {
    console.info('Cleanup…');
    // Cleanup the directory to initialize the process.
    fs.rm(kpiDirName, {recursive: true}, (err) => {
      if (err) {throw err;}
      console.info('Cleanup done.');
      getKpiFiles();
    });
  }
  else {
    getKpiFiles();
  }
}

start()
