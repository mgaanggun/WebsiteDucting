const fs = require('fs');
const path = require('path');
const root = 'c:/Constructify-pro';
const files = fs.readdirSync(root).filter(f => f.endsWith('.html'));

let count = 0;
files.forEach(f => {
  const content = fs.readFileSync(path.join(root, f), 'utf8');
  const matches = content.match(/["'][^"']*\.jpe?g["']/gi);
  if (matches) {
    matches.forEach(m => {
      if (!m.includes('assets/img/ducting/')) {
        console.log(`OTHER JPG in ${f}: ${m}`);
        count++;
      }
    });
  }
});
console.log(`Total non-ducting JPG occurrences: ${count}`);
