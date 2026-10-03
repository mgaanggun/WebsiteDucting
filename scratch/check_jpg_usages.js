const fs = require('fs');
const path = require('path');

const root = 'c:/Constructify-pro';
const files = fs.readdirSync(root).filter(f => f.endsWith('.html'));

files.forEach(f => {
  const content = fs.readFileSync(path.join(root, f), 'utf8');
  const lines = content.split('\n');
  lines.forEach((line, idx) => {
    if (line.includes('.jpg') || line.includes('.jpeg')) {
      console.log(`${f}:${idx + 1}: ${line.trim()}`);
    }
  });
});
