const { generateFonts } = require('fantasticon');
const fs = require('fs');
const path = require('path');
const simpleGit = require('simple-git');

const kpiDirName = 'temp-kpi-clone';
const sourceDir = path.join(kpiDirName, 'jsapp/svg-icons');
const destDir = path.join('source/_static/kpi-icons');
const cssTemplatePath = path.join(kpiDirName, 'jsapp/k-icons-css-template.hbs');

const git = simpleGit({
  baseDir: process.cwd(),
  binary: 'git',
  maxConcurrentProcesses: 6,
});

async function generateIconsFromKpiFiles() {
  fs.mkdirSync(destDir, {recursive: true});

  console.info('Generating fonts…');
  await generateFonts({
    name: 'k-icons',
    inputDir: sourceDir,
    outputDir: destDir,
    fontTypes: ['eot', 'svg', 'ttf', 'woff', 'woff2'],
    assetTypes: ['css', 'html'],
    prefix: 'k-icon',
    selector: '.k-icon',
    // CSS and fonts live in the same directory, so no path prefix needed.
    fontsUrl: '.',
    normalize: false,
    fontHeight: 10000,
    descent: 0,
    round: 0,
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
        ascent: undefined,
      },
    },
    templates: {
      css: cssTemplatePath,
      html: undefined,
    },
  });

  console.info('Cleanup…');
  await fs.promises.rm(kpiDirName, {recursive: true});
  console.info('Icons generated successfully!');
}

function getKpiFiles() {
  console.info('Cloning kpi repository…');
  return git.clone('https://github.com/kobotoolbox/kpi', kpiDirName, {
    '--single-branch': true,
    '--depth': 1,
  });
}

async function start() {
  await fs.promises.rm(kpiDirName, {recursive: true, force: true});
  await getKpiFiles();
  await generateIconsFromKpiFiles();
}

start().catch((error) => {
  console.error('Icon generation failed:', error);
  process.exit(1);
});
