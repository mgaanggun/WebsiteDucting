const fs = require('fs');
const path = require('path');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
let brokenCount = 0;

files.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  const regex = /href=["']([^"'#?]+\.html)["']/g;
  let match;
  while ((match = regex.exec(content)) !== null) {
    const target = match[1];
    if (!target.startsWith('http') && !target.startsWith('//')) {
      if (!fs.existsSync(target)) {
        console.log(`[BROKEN LINK] in ${file}: ${target}`);
        brokenCount++;
      }
    }
  }
});

console.log(`Total broken links: ${brokenCount}`);
