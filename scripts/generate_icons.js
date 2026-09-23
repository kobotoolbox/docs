// Generates two icon fonts used by the docs:
//
// 1. k-icons — KoboToolbox's custom icon set, built from SVGs in the KPI repo.
// 2. tabler-* — A subset of the Tabler icon webfont containing only the icons
//    listed in tabler-icons-list.json. Add icons there as KPI
//    migrates more of its icons to Tabler.
//

const { generateFonts } = require('fantasticon');
const fs = require('fs');
const path = require('path');
const simpleGit = require('simple-git');
const subsetFont = require('subset-font');

const kpiDirName = 'temp-kpi-clone';
const sourceDir = path.join(kpiDirName, 'jsapp/svg-icons');
const destDir = path.join('source/_static/kpi-icons');
const cssTemplatePath = path.join(kpiDirName, 'jsapp/k-icons-css-template.hbs');

const tablerWebfontDir = path.join('node_modules/@tabler/icons-webfont/dist');
const tablerDestDir = path.join('source/_static/tabler-icons');
const tablerIconsList = require('./tabler-icons-list.json');

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

// Parses the codepoint map from a Tabler webfont CSS file: {icon-name -> codepoint}.
function parseTablerCodepoints(cssFile) {
  const css = fs.readFileSync(cssFile, 'utf8');
  const map = {};
  const re = /\.ti-([a-z0-9-]+):before\s*\{\s*content:\s*"\\([0-9a-f]+)"/g;
  let match;
  while ((match = re.exec(css)) !== null) {
    map[match[1]] = parseInt(match[2], 16);
  }
  return map;
}

function buildTablerCss(variant, icons, codepointMap) {
  const fontFile = `tabler-${variant}`;
  const lines = [
    `@font-face {`,
    `  font-family: "${fontFile}";`,
    `  src: url('./${fontFile}.woff2') format('woff2'), url('./${fontFile}.woff') format('woff');`,
    `  font-weight: normal;`,
    `  font-style: normal;`,
    `}`,
    ``,
    `.ti-${variant} {`,
    `  font-family: "${fontFile}";`,
    `  font-style: normal;`,
    `  font-weight: normal;`,
    `  speak: none;`,
    `  -webkit-font-smoothing: antialiased;`,
    `  -moz-osx-font-smoothing: grayscale;`,
    `}`,
    ``,
  ];
  for (const name of icons) {
    const cp = codepointMap[name];
    if (cp) {
      lines.push(`.ti-${variant}.ti-${name}:before { content: "\\${cp.toString(16)}"; }`);
    }
  }
  return lines.join('\n');
}

// Subsets the Tabler webfont to only the icons in tabler-icons-list.json.
// We subset rather than generate from SVGs because Tabler's outline icons are
// stroke-based, which don't convert correctly to a font via fantasticon. The
// webfont package has already done that conversion properly.
async function generateTablerIcons() {
  console.info('Generating Tabler icons…');
  await fs.promises.rm(tablerDestDir, {recursive: true, force: true});
  fs.mkdirSync(tablerDestDir, {recursive: true});

  const srcCssFiles = {
    outline: path.join(tablerWebfontDir, 'tabler-icons.css'),
    filled: path.join(tablerWebfontDir, 'tabler-icons-filled.css'),
  };
  const srcFontFiles = {
    outline: path.join(tablerWebfontDir, 'fonts', 'tabler-icons.woff2'),
    filled: path.join(tablerWebfontDir, 'fonts', 'tabler-icons-filled.woff2'),
  };

  for (const variant of ['outline', 'filled']) {
    const icons = tablerIconsList[variant];
    const codepointMap = parseTablerCodepoints(srcCssFiles[variant]);
    const codepoints = icons.map(n => codepointMap[n]).filter(Boolean);

    const srcFont = await fs.promises.readFile(srcFontFiles[variant]);
    const glyphText = codepoints.map(cp => String.fromCodePoint(cp)).join('');
    const subsetted = await subsetFont(srcFont, glyphText, {targetFormat: 'woff2'});
    await fs.promises.writeFile(path.join(tablerDestDir, `tabler-${variant}.woff2`), subsetted);

    // Also generate woff for older browser fallback
    const subsettedWoff = await subsetFont(srcFont, glyphText, {targetFormat: 'woff'});
    await fs.promises.writeFile(path.join(tablerDestDir, `tabler-${variant}.woff`), subsettedWoff);

    const css = buildTablerCss(variant, icons, codepointMap);
    await fs.promises.writeFile(path.join(tablerDestDir, `tabler-${variant}.css`), css);
  }

  console.info('Tabler icons generated successfully!');
}

async function start() {
  await fs.promises.rm(kpiDirName, {recursive: true, force: true});
  await getKpiFiles();
  await generateIconsFromKpiFiles();
  await generateTablerIcons();
}

start().catch((error) => {
  console.error('Icon generation failed:', error);
  process.exit(1);
});
