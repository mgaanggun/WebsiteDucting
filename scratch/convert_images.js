const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const dir = path.join(__dirname, '../assets/img/ducting');
const files = fs.readdirSync(dir).filter(f => /\.jpe?g$/i.test(f));

console.log(`Found ${files.length} JPG files to convert.`);

async function convertAll() {
  const results = [];
  for (const file of files) {
    const inputPath = path.join(dir, file);
    const baseName = path.parse(file).name;
    const outputPath = path.join(dir, `${baseName}.webp`);

    const metaBefore = await sharp(inputPath).metadata();
    
    // Resize to exact 1200x675 using high-quality lanczos3 filter with fit cover
    await sharp(inputPath)
      .resize(1200, 675, {
        fit: 'cover',
        position: 'center'
      })
      .webp({
        quality: 85,
        effort: 6
      })
      .toFile(outputPath);

    const metaAfter = await sharp(outputPath).metadata();
    const statsBefore = fs.statSync(inputPath);
    const statsAfter = fs.statSync(outputPath);

    results.push({
      file,
      output: `${baseName}.webp`,
      before: `${metaBefore.width}x${metaBefore.height} (${(statsBefore.size / 1024).toFixed(1)} KB)`,
      after: `${metaAfter.width}x${metaAfter.height} (${(statsAfter.size / 1024).toFixed(1)} KB)`
    });
  }

  console.table(results);
}

convertAll().catch(err => {
  console.error('Error during conversion:', err);
  process.exit(1);
});
