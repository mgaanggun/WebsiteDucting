const fs = require('fs');
const path = require('path');

const root = 'c:/Constructify-pro';
const files = fs.readdirSync(root).filter(f => f.endsWith('.html'));

const types = {};

files.forEach(f => {
  const content = fs.readFileSync(path.join(root, f), 'utf8');
  const lines = content.split('\n');
  lines.forEach((line, idx) => {
    if (line.includes('.jpg') || line.includes('.jpeg')) {
      const trimmed = line.trim();
      let tag = 'other';
      if (trimmed.startsWith('<img') || trimmed.includes('<img')) tag = 'img';
      else if (trimmed.startsWith('<a') || trimmed.includes('<a')) tag = 'a';
      else if (trimmed.includes('<meta')) tag = 'meta';
      else if (trimmed.includes('"image"')) tag = 'jsonld';
      
      if (!types[tag]) types[tag] = [];
      types[tag].push(`${f}:${idx + 1}: ${trimmed}`);
    }
  });
});

for (const [t, items] of Object.entries(types)) {
  console.log(`=== Tag: ${t} (${items.length} occurrences) ===`);
  items.slice(0, 5).forEach(i => console.log('  ' + i));
}
