const fs = require('fs');
const path = require('path');

const root = 'c:/Constructify-pro';
const files = fs.readdirSync(root).filter(f => f.endsWith('.html'));

let totalReplacements = 0;
const report = [];

files.forEach(file => {
  const filePath = path.join(root, file);
  const content = fs.readFileSync(filePath, 'utf8');

  let fileReplacements = 0;
  const updatedContent = content.replace(/assets\/img\/ducting\/([a-zA-Z0-9_\-]+)\.jpg/gi, (match, baseName) => {
    fileReplacements++;
    return `assets/img/ducting/${baseName}.webp`;
  });

  if (fileReplacements > 0) {
    fs.writeFileSync(filePath, updatedContent, 'utf8');
    totalReplacements += fileReplacements;
    report.push({ file, replacements: fileReplacements });
  }
});

console.log(`Updated ${report.length} HTML files with a total of ${totalReplacements} replacements.`);
console.table(report);
